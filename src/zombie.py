"""
SHOOT 'EM UP - Zombie Classes
Chứa class Zombie và ZombieManager
"""

import pygame
import random
import math
from .settings import *


class Zombie:
    """Class đại diện cho một zombie"""
    
    def __init__(self, x, y, zombie_type="small"):
        """Initialize zombie"""
        self.x = x
        self.y = y
        self.type = zombie_type
        self.lifetime = ZOMBIE_LIFETIME
        self.alive = True
        
        # Set size based on type
        if zombie_type == "small":
            self.size = ZOMBIE_SMALL_SIZE
            self.color = RED
        else:  # large
            self.size = ZOMBIE_LARGE_SIZE  
            self.color = (200, 0, 0)  # Darker red
        
        # Create rect for collision detection
        self.rect = pygame.Rect(x - self.size[0]//2, y - self.size[1]//2, 
                               self.size[0], self.size[1])
        
        # Create surface (tạm thời dùng hình chữ nhật màu)
        self.surface = pygame.Surface(self.size)
        self.surface.fill(self.color)
        
        # Add border
        pygame.draw.rect(self.surface, WHITE, self.surface.get_rect(), 2)
    
    def update(self, dt):
        """Update zombie"""
        if not self.alive:
            return
            
        # Decrease lifetime
        self.lifetime -= dt
        
        # Check if zombie should disappear
        if self.lifetime <= 0:
            self.alive = False
    
    def draw(self, screen):
        """Draw zombie"""
        if not self.alive:
            return
            
        # Calculate alpha for fade effect
        alpha = min(255, int(255 * (self.lifetime / ZOMBIE_LIFETIME)))
        
        # Apply alpha
        temp_surface = self.surface.copy()
        temp_surface.set_alpha(alpha)
        
        # Draw
        screen.blit(temp_surface, self.rect)
    
    def is_clicked(self, pos):
        """Check if zombie was clicked"""
        return self.alive and self.rect.collidepoint(pos)


class ZombieManager:
    """Class quản lý tất cả zombies"""
    
    def __init__(self):
        """Initialize zombie manager"""
        self.zombies = []
        self.spawn_timer = 0
        self.current_spawn_rate = INITIAL_SPAWN_RATE
    
    def reset(self):
        """Reset zombie manager"""
        self.zombies.clear()
        self.spawn_timer = 0
        self.current_spawn_rate = INITIAL_SPAWN_RATE
    
    def update(self, dt, game_time_left):
        """Update all zombies and spawning"""
        # Update spawn rate based on remaining time
        progress = 1.0 - (game_time_left / GAME_DURATION)
        self.current_spawn_rate = INITIAL_SPAWN_RATE - (INITIAL_SPAWN_RATE - MIN_SPAWN_RATE) * progress
        
        # Update spawn timer
        self.spawn_timer -= dt
        
        # Spawn new zombies if needed
        if self.spawn_timer <= 0:
            self._spawn_zombies_group(progress)
            self.spawn_timer = self.current_spawn_rate
        
        # Update existing zombies
        for zombie in self.zombies[:]:  # Copy list to avoid modification during iteration
            zombie.update(dt)
            if not zombie.alive:
                self.zombies.remove(zombie)
    
    def _spawn_zombies_group(self, progress):
        """Spawn a group of zombies based on game progress"""
        # Count current alive zombies
        alive_zombies = len([z for z in self.zombies if z.alive])
        
        # Don't spawn if we're at max capacity
        if alive_zombies >= MAX_ZOMBIES_ON_SCREEN:
            return
        
        # Determine how many zombies to spawn based on progress
        if progress < 0.3:  # Early game (0-30%)
            max_spawn = MIN_ZOMBIES_PER_SPAWN
        elif progress < 0.6:  # Mid game (30-60%)
            max_spawn = MAX_ZOMBIES_PER_SPAWN
        else:  # Late game (60%+)
            max_spawn = LATE_GAME_MAX_SPAWN
        
        # Calculate actual spawn count
        available_slots = MAX_ZOMBIES_ON_SCREEN - alive_zombies
        spawn_count = min(
            random.randint(MIN_ZOMBIES_PER_SPAWN, max_spawn),
            available_slots
        )
        
        # Spawn the zombies
        positions = self._generate_spawn_positions(spawn_count)
        for pos in positions:
            zombie_type = random.choice(["small", "large"])
            zombie = Zombie(pos[0], pos[1], zombie_type)
            self.zombies.append(zombie)
    
    def _generate_spawn_positions(self, count):
        """Generate clustered spawn positions - zombies spawn near each other"""
        if count <= 0:
            return []
            
        positions = []
        
        # Generate cluster center (avoid existing zombies)
        cluster_center = self._find_cluster_center()
        
        # Define cluster parameters
        cluster_radius = CLUSTER_RADIUS      # Radius of the cluster area
        min_distance = MIN_CLUSTER_DISTANCE  # Minimum distance between zombies in cluster
        max_attempts = 30
        
        for i in range(count):
            attempts = 0
            position_found = False
            
            while attempts < max_attempts and not position_found:
                if i == 0:
                    # First zombie spawns at or near cluster center
                    angle = random.uniform(0, 2 * math.pi)
                    distance = random.uniform(0, CLUSTER_CENTER_VARIATION)  # Very close to center
                    x = cluster_center[0] + distance * math.cos(angle)
                    y = cluster_center[1] + distance * math.sin(angle)
                else:
                    # Other zombies spawn around the cluster
                    angle = random.uniform(0, 2 * math.pi)
                    distance = random.uniform(40, cluster_radius)
                    x = cluster_center[0] + distance * math.cos(angle)
                    y = cluster_center[1] + distance * math.sin(angle)
                
                # Ensure position is within screen bounds
                x = max(ZOMBIE_SPAWN_MARGIN, min(SCREEN_WIDTH - ZOMBIE_SPAWN_MARGIN, x))
                y = max(ZOMBIE_SPAWN_MARGIN, min(SCREEN_HEIGHT - ZOMBIE_SPAWN_MARGIN, y))
                
                # Check minimum distance from other positions in this spawn
                valid_position = True
                for existing_pos in positions:
                    distance_to_existing = math.sqrt((x - existing_pos[0])**2 + (y - existing_pos[1])**2)
                    if distance_to_existing < min_distance:
                        valid_position = False
                        break
                
                # Check distance from existing alive zombies
                if valid_position:
                    for zombie in self.zombies:
                        if zombie.alive:
                            zombie_distance = math.sqrt((x - zombie.x)**2 + (y - zombie.y)**2)
                            if zombie_distance < min_distance:
                                valid_position = False
                                break
                
                if valid_position:
                    positions.append((x, y))
                    position_found = True
                
                attempts += 1
            
            # Fallback: if couldn't find good position, use a safe random position
            if not position_found:
                safe_x = random.randint(ZOMBIE_SPAWN_MARGIN, SCREEN_WIDTH - ZOMBIE_SPAWN_MARGIN)
                safe_y = random.randint(ZOMBIE_SPAWN_MARGIN, SCREEN_HEIGHT - ZOMBIE_SPAWN_MARGIN)
                positions.append((safe_x, safe_y))
        
        return positions
    
    def _find_cluster_center(self):
        """Find a good center position for zombie cluster"""
        max_attempts = 20
        best_center = None
        best_score = -1
        
        for _ in range(max_attempts):
            # Random center position (with margin for cluster radius)
            margin = ZOMBIE_SPAWN_MARGIN + CLUSTER_RADIUS
            center_x = random.randint(margin, SCREEN_WIDTH - margin)
            center_y = random.randint(margin, SCREEN_HEIGHT - margin)
            
            # Calculate score based on distance from existing zombies
            score = 0
            for zombie in self.zombies:
                if zombie.alive:
                    distance = math.sqrt((center_x - zombie.x)**2 + (center_y - zombie.y)**2)
                    score += distance  # Higher score = farther from existing zombies
            
            if score > best_score:
                best_score = score
                best_center = (center_x, center_y)
        
        # Fallback to center of screen if no good position found
        if best_center is None:
            best_center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            
        return best_center
    
    def _spawn_zombie(self):
        """Spawn a single zombie at random position (legacy method)"""
        # Random position with margin from edges
        x = random.randint(ZOMBIE_SPAWN_MARGIN, SCREEN_WIDTH - ZOMBIE_SPAWN_MARGIN)
        y = random.randint(ZOMBIE_SPAWN_MARGIN, SCREEN_HEIGHT - ZOMBIE_SPAWN_MARGIN)
        
        # Random type (50% chance for each)
        zombie_type = random.choice(["small", "large"])
        
        # Create and add zombie
        zombie = Zombie(x, y, zombie_type)
        self.zombies.append(zombie)
    
    def draw(self, screen):
        """Draw all zombies"""
        for zombie in self.zombies:
            zombie.draw(screen)
    
    def check_hit(self, pos):
        """Check if a click hit any zombie"""
        for zombie in self.zombies[:]:
            if zombie.is_clicked(pos):
                zombie.alive = False
                return True
        return False
    
    def get_alive_count(self):
        """Get count of alive zombies"""
        return len([z for z in self.zombies if z.alive])
    
    def get_total_count(self):
        """Get total count of zombies"""
        return len(self.zombies)
