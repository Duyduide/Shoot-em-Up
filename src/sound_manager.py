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
        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.mixer.init()
        
        # Sound effects
        self.shoot_sound = None
        self.hit_sound = None
        
        # Background music
        self.theme_music_loaded = False
        
        # Load sounds
        self._load_sounds()
    
    def _load_sounds(self):
        """Load sound effects"""
        try:
            # Load sound effects
            self.shoot_sound = pygame.mixer.Sound(SHOOT_SOUND)
            self.hit_sound = pygame.mixer.Sound(HIT_SOUND)
            
            # Load background music
            pygame.mixer.music.load(THEME_MUSIC)
            self.theme_music_loaded = True
            
            print("✅ All sound files loaded successfully!")
            
        except Exception as e:
            print(f"⚠️ Warning: Could not load some sound files: {e}")
            # Create fallback silence sounds if loading fails
            try:
                self.shoot_sound = pygame.mixer.Sound(buffer=bytes(1024))
                self.hit_sound = pygame.mixer.Sound(buffer=bytes(1024))
            except:
                pass
    
    def play_shoot(self):
        """Play shoot sound"""
        if self.shoot_sound:
            self.shoot_sound.play()
    
    def play_hit(self):
        """Play hit sound"""
        if self.hit_sound:
            self.hit_sound.play()
    
    def play_theme_music(self, loop=-1):
        """Play background theme music"""
        if self.theme_music_loaded:
            try:
                pygame.mixer.music.play(loop)  # loop=-1 means infinite loop
            except Exception as e:
                print(f"Could not play theme music: {e}")
    
    def stop_theme_music(self):
        """Stop background music"""
        pygame.mixer.music.stop()
    
    def pause_theme_music(self):
        """Pause background music"""
        pygame.mixer.music.pause()
    
    def resume_theme_music(self):
        """Resume background music"""
        pygame.mixer.music.unpause()
    
    def set_music_volume(self, volume):
        """Set music volume (0.0 to 1.0)"""
        pygame.mixer.music.set_volume(volume)
    
    def set_sfx_volume(self, volume):
        """Set sound effects volume (0.0 to 1.0)"""
        if self.shoot_sound:
            self.shoot_sound.set_volume(volume)
        if self.hit_sound:
            self.hit_sound.set_volume(volume)
