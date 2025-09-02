"""
SHOOT 'EM UP - Zombie Classes
Chứa class Zombie và ZombieManager
"""

import pygame
import random
import math
from .settings import *


class Zombie:
    """Class đại diện cho một zombie với sprite animation system"""
    
    # Class variables to share loaded images between all zombies
    idle_images_small = None
    idle_images_large = None
    hit_images_small = None
    hit_images_large = None
    images_loaded = False
    
    @classmethod
    def load_zombie_images(cls):
        """Load zombie images once for all instances"""
        if cls.images_loaded:
            return
            
        print("🔄 Loading zombie sprite animations...")
        
        # Load idle animation frames
        cls.idle_images_small = []
        cls.idle_images_large = []
        
        try:
            for image_path in ZOMBIE_IDLE_IMAGES:
                img = pygame.image.load(image_path).convert_alpha()
                
                # Scale for small zombies
                scaled_small = pygame.transform.scale(img, ZOMBIE_SMALL_SIZE)
                cls.idle_images_small.append(scaled_small)
                
                # Scale for large zombies
                scaled_large = pygame.transform.scale(img, ZOMBIE_LARGE_SIZE)
                cls.idle_images_large.append(scaled_large)
            
            print(f"✅ Loaded {len(cls.idle_images_small)} idle animation frames")
        except Exception as e:
            print(f"⚠️ Warning: Could not load idle images: {e}")
            cls._create_fallback_idle_images()
        
        # Load hit animation frames
        cls.hit_images_small = []
        cls.hit_images_large = []
        
        try:
            for image_path in ZOMBIE_HIT_IMAGES:
                img = pygame.image.load(image_path).convert_alpha()
                
                # Scale for small zombies
                scaled_small = pygame.transform.scale(img, ZOMBIE_SMALL_SIZE)
                cls.hit_images_small.append(scaled_small)
                
                # Scale for large zombies
                scaled_large = pygame.transform.scale(img, ZOMBIE_LARGE_SIZE)
                cls.hit_images_large.append(scaled_large)
            
            print(f"✅ Loaded {len(cls.hit_images_small)} hit animation frames")
        except Exception as e:
            print(f"⚠️ Warning: Could not load hit images: {e}")
            cls._create_fallback_hit_images()
        
        cls.images_loaded = True
        print("🎨 Zombie sprite system initialized!")
    
    @classmethod
    def _create_fallback_idle_images(cls):
        """Create fallback idle animation if images fail to load"""
        colors = [(255, 100, 100), (255, 120, 120), (255, 140, 140), (255, 120, 120), (255, 100, 100)]
        
        cls.idle_images_small = []
        cls.idle_images_large = []
        
        for color in colors:
            # Small fallback
            surface_small = pygame.Surface(ZOMBIE_SMALL_SIZE)
            surface_small.fill(color)
            pygame.draw.rect(surface_small, WHITE, surface_small.get_rect(), 2)
            cls.idle_images_small.append(surface_small)
            
            # Large fallback
            surface_large = pygame.Surface(ZOMBIE_LARGE_SIZE)
            surface_large.fill(color)
            pygame.draw.rect(surface_large, WHITE, surface_large.get_rect(), 2)
            cls.idle_images_large.append(surface_large)
    
    @classmethod
    def _create_fallback_hit_images(cls):
        """Create fallback hit animation if images fail to load"""
        colors = [(255, 0, 0), (255, 50, 50), (255, 100, 100), (255, 150, 150)]
        
        cls.hit_images_small = []
        cls.hit_images_large = []
        
        for i, color in enumerate(colors):
            # Small fallback
            surface_small = pygame.Surface(ZOMBIE_SMALL_SIZE)
            surface_small.fill(color)
            pygame.draw.rect(surface_small, WHITE, surface_small.get_rect(), 2)
            if i > 0:  # Add X for hit effect
                pygame.draw.line(surface_small, BLACK, (5, 5), (ZOMBIE_SMALL_SIZE[0]-5, ZOMBIE_SMALL_SIZE[1]-5), 2)
                pygame.draw.line(surface_small, BLACK, (ZOMBIE_SMALL_SIZE[0]-5, 5), (5, ZOMBIE_SMALL_SIZE[1]-5), 2)
            cls.hit_images_small.append(surface_small)
            
            # Large fallback
            surface_large = pygame.Surface(ZOMBIE_LARGE_SIZE)
            surface_large.fill(color)
            pygame.draw.rect(surface_large, WHITE, surface_large.get_rect(), 2)
            if i > 0:  # Add X for hit effect
                pygame.draw.line(surface_large, BLACK, (5, 5), (ZOMBIE_LARGE_SIZE[0]-5, ZOMBIE_LARGE_SIZE[1]-5), 3)
                pygame.draw.line(surface_large, BLACK, (ZOMBIE_LARGE_SIZE[0]-5, 5), (5, ZOMBIE_LARGE_SIZE[1]-5), 3)
            cls.hit_images_large.append(surface_large)
    
    def __init__(self, x, y, zombie_type="small"):
        """Initialize zombie with sprite animation system"""
        # Load shared images if not already loaded
        if not Zombie.images_loaded:
            Zombie.load_zombie_images()
        
        self.x = x
        self.y = y
        self.type = zombie_type
        self.lifetime = ZOMBIE_LIFETIME
        self.alive = True
        
        # Animation states
        self.is_hit = False
        self.hit_animation_timer = 0
        self.idle_animation_timer = 0
        self.current_idle_frame = 0
        self.current_hit_frame = 0
        
        # Set size and get references to appropriate images
        if zombie_type == "small":
            self.size = ZOMBIE_SMALL_SIZE
            self.idle_images = Zombie.idle_images_small
            self.hit_images = Zombie.hit_images_small
        else:
            self.size = ZOMBIE_LARGE_SIZE
            self.idle_images = Zombie.idle_images_large
            self.hit_images = Zombie.hit_images_large
        
        # Create rect for collision detection
        self.rect = pygame.Rect(x - self.size[0]//2, y - self.size[1]//2, 
                               self.size[0], self.size[1])
    
    def update(self, dt):
        """Update zombie with sprite animations"""
        if not self.alive:
            return
        
        if self.is_hit:
            # Update hit animation
            self.hit_animation_timer += dt
            
            # Calculate hit animation frame
            frame_index = int(self.hit_animation_timer / ZOMBIE_HIT_FRAME_DURATION)
            self.current_hit_frame = min(frame_index, len(self.hit_images) - 1)
            
            # Check if hit animation is complete
            if self.hit_animation_timer >= ZOMBIE_HIT_ANIMATION_DURATION:
                self.alive = False
                return
        else:
            # Update idle animation
            self.idle_animation_timer += dt
            
            # Calculate idle animation frame (loops continuously)
            total_idle_frames = len(self.idle_images)
            if total_idle_frames > 0:
                frame_index = int(self.idle_animation_timer / ZOMBIE_IDLE_ANIMATION_SPEED) % total_idle_frames
                self.current_idle_frame = frame_index
        
        # Decrease lifetime (only if not hit)
        if not self.is_hit:
            self.lifetime -= dt
            
            # Check if zombie should disappear
            if self.lifetime <= 0:
                self.alive = False
    
    def hit(self):
        """Register zombie being hit and start death animation"""
        if self.is_hit:
            return False  # Already hit
        
        self.is_hit = True
        self.hit_animation_timer = 0
        self.current_hit_frame = 0
        return True
    
    def draw(self, screen):
        """Draw zombie with sprite animation"""
        if not self.alive:
            return
        
        # Select current image based on animation state
        if self.is_hit:
            if self.hit_images and self.current_hit_frame < len(self.hit_images):
                current_image = self.hit_images[self.current_hit_frame]
            else:
                return  # No hit images available
        else:
            if self.idle_images and self.current_idle_frame < len(self.idle_images):
                current_image = self.idle_images[self.current_idle_frame]
            else:
                return  # No idle images available
        
        # Apply fade effect for idle zombies based on lifetime
        if not self.is_hit:
            alpha = min(255, int(255 * (self.lifetime / ZOMBIE_LIFETIME)))
            if alpha < 255:
                # Create a copy and apply alpha
                temp_surface = current_image.copy()
                temp_surface.set_alpha(alpha)
                current_image = temp_surface
        
        # Draw the zombie sprite
        screen.blit(current_image, self.rect)
    
    def hit(self):
        """Mark zombie as hit and start death animation"""
        if not self.is_hit:
            self.is_hit = True
            self.hit_animation_timer = 0
            self.current_hit_frame = 0  # Start with first hit frame
    
    def is_clicked(self, pos):
        """Check if zombie was clicked"""
        return self.alive and not self.is_hit and self.rect.collidepoint(pos)


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
                zombie.hit()  # Start hit animation instead of immediate death
                return True
        return False
    
    def get_alive_count(self):
        """Get count of alive zombies (not including those being hit)"""
        return len([z for z in self.zombies if z.alive and not z.is_hit])
    
    def get_total_count(self):
        """Get total count of zombies"""
        return len(self.zombies)
