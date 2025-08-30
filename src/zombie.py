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
        
        # Spawn new zombie if needed
        if self.spawn_timer <= 0:
            self._spawn_zombie()
            self.spawn_timer = self.current_spawn_rate
        
        # Update existing zombies
        for zombie in self.zombies[:]:  # Copy list to avoid modification during iteration
            zombie.update(dt)
            if not zombie.alive:
                self.zombies.remove(zombie)
    
    def _spawn_zombie(self):
        """Spawn a new zombie at random position"""
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
