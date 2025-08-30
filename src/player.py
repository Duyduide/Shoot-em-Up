"""
SHOOT 'EM UP - Player Input Manager
Quản lý input của người chơi (tạm thời đơn giản, có thể mở rộng sau)
"""

import pygame


class Player:
    """Class quản lý input và stats của player"""
    
    def __init__(self):
        """Initialize player"""
        self.score = 0
        self.hits = 0
        self.misses = 0
        self.total_shots = 0
        
        # Input state
        self.mouse_pos = (0, 0)
        self.mouse_clicked = False
    
    def update_input(self):
        """Update input state"""
        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_clicked = pygame.mouse.get_pressed()[0]
    
    def add_hit(self, points=10):
        """Add a hit"""
        self.hits += 1
        self.total_shots += 1
        self.score += points
    
    def add_miss(self, penalty=0):
        """Add a miss"""
        self.misses += 1
        self.total_shots += 1
        self.score -= penalty
    
    def get_accuracy(self):
        """Get current accuracy percentage"""
        if self.total_shots == 0:
            return 0.0
        return (self.hits / self.total_shots) * 100.0
    
    def reset_stats(self):
        """Reset player stats"""
        self.score = 0
        self.hits = 0
        self.misses = 0
        self.total_shots = 0
