"""
SHOOT 'EM UP - Sound Manager
Quản lý âm thanh của game
"""

import pygame
from .settings import *


class SoundManager:
    """Class quản lý âm thanh"""
    
    def __init__(self):
        """Initialize sound manager"""
        # Initialize pygame mixer
        pygame.mixer.init()
        
        # Sound effects (tạm thời để trống, sẽ load sau khi có file audio)
        self.shoot_sound = None
        self.hit_sound = None
        self.miss_sound = None
        
        # Load sounds
        self._load_sounds()
    
    def _load_sounds(self):
        """Load sound effects"""
        try:
            # Tạm thời comment out vì chưa có file audio
            # self.shoot_sound = pygame.mixer.Sound(SHOOT_SOUND)
            # self.hit_sound = pygame.mixer.Sound(HIT_SOUND)
            # self.miss_sound = pygame.mixer.Sound(MISS_SOUND)
            pass
        except Exception as e:
            print(f"Warning: Could not load sound files: {e}")
    
    def play_shoot(self):
        """Play shoot sound"""
        if self.shoot_sound:
            self.shoot_sound.play()
    
    def play_hit(self):
        """Play hit sound"""
        if self.hit_sound:
            self.hit_sound.play()
    
    def play_miss(self):
        """Play miss sound"""
        if self.miss_sound:
            self.miss_sound.play()
    
    def set_volume(self, volume):
        """Set overall volume (0.0 to 1.0)"""
        pygame.mixer.music.set_volume(volume)
