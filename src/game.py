"""
SHOOT 'EM UP - Main Game Class
Class chính quản lý toàn bộ game loop và states
"""

import pygame
import sys
from .settings import *
from .ui import UI
from .zombie import ZombieManager
from .sound_manager import SoundManager


class Game:
    """Main game class quản lý game loop và states"""
    
    def __init__(self):
        """Initialize game"""
        # Screen setup
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("SHOOT 'EM UP")
        self.clock = pygame.time.Clock()
        
        # Game state
        self.state = MENU_STATE
        self.running = True
        
        # Game components
        self.ui = UI(self.screen)
        self.zombie_manager = ZombieManager()
        self.sound_manager = SoundManager()
        
        # Game variables
        self.score = 0
        self.hits = 0
        self.total_shots = 0
        self.game_timer = 0
        
        # Load assets
        self._load_assets()
        
        # Start background music
        self.sound_manager.set_music_volume(0.3)  # Set to 30% volume
        self.sound_manager.set_sfx_volume(0.5)    # Set SFX to 50% volume
        self.sound_manager.play_theme_music()     # Start playing theme music
        
    def _load_assets(self):
        """Load game assets"""
        try:
            # Load background (tạm thời dùng màu đen)
            self.background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            self.background.fill(BLACK)
            
            # Load crosshair image
            try:
                crosshair_original = pygame.image.load(CROSSHAIR_IMAGE).convert_alpha()
                # Scale crosshair to smaller size (24x24 instead of original size)
                self.crosshair_surface = pygame.transform.scale(crosshair_original, (64, 64))
                print("✅ Crosshair image loaded and scaled successfully!")
            except Exception as crosshair_error:
                print(f"Warning: Could not load crosshair image: {crosshair_error}")
                # Fallback to drawn crosshair (smaller size)
                self.crosshair_surface = pygame.Surface((64, 64), pygame.SRCALPHA)
                pygame.draw.circle(self.crosshair_surface, WHITE, (12, 12), 10, 2)
                pygame.draw.circle(self.crosshair_surface, WHITE, (12, 12), 1)
            
        except Exception as e:
            print(f"Warning: Could not load some assets: {e}")
    
    def run(self):
        """Main game loop"""
        while self.running:
            dt = self.clock.tick(FPS) / 1000.0  # Delta time in seconds
            
            # Handle events
            self._handle_events()
            
            # Update game state
            self._update(dt)
            
            # Render
            self._render()
    
    def _handle_events(self):
        """Handle pygame events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.state == PLAYING_STATE:
                        self.state = MENU_STATE
                    else:
                        self.running = False
                elif event.key == pygame.K_m:  # Toggle music mute
                    current_volume = pygame.mixer.music.get_volume()
                    if current_volume > 0:
                        pygame.mixer.music.set_volume(0)
                    else:
                        self.sound_manager.set_music_volume(0.3)
                elif event.key == pygame.K_p:  # Pause/Resume music
                    if pygame.mixer.music.get_busy():
                        self.sound_manager.pause_theme_music()
                    else:
                        self.sound_manager.resume_theme_music()
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    self._handle_click(event.pos)
    
    def _handle_click(self, pos):
        """Handle mouse click"""
        if self.state == MENU_STATE:
            # Check menu buttons
            button_clicked = self.ui.handle_menu_click(pos)
            if button_clicked == "play":
                self._start_game()
            elif button_clicked == "quit":
                self.running = False
                
        elif self.state == PLAYING_STATE:
            # Shoot at zombies
            self.total_shots += 1
            hit = self.zombie_manager.check_hit(pos)
            
            if hit:
                self.hits += 1
                self.score += HIT_POINTS
                self.sound_manager.play_hit()
            else:
                self.score += MISS_PENALTY
                # No miss sound as requested
            
            self.sound_manager.play_shoot()
            
        elif self.state == GAME_OVER_STATE:
            # Check if clicked to return to menu
            self.state = MENU_STATE
    
    def _start_game(self):
        """Start new game"""
        self.state = PLAYING_STATE
        self.score = 0
        self.hits = 0
        self.total_shots = 0
        self.game_timer = GAME_DURATION
        self.zombie_manager.reset()
    
    def _update(self, dt):
        """Update game state"""
        if self.state == PLAYING_STATE:
            # Update game timer
            self.game_timer -= dt
            
            # Check game over
            if self.game_timer <= 0:
                self.state = GAME_OVER_STATE
                return
            
            # Update zombies
            self.zombie_manager.update(dt, self.game_timer)
    
    def _render(self):
        """Render game"""
        # Clear screen
        self.screen.blit(self.background, (0, 0))
        
        if self.state == MENU_STATE:
            self.ui.draw_menu()
            
        elif self.state == PLAYING_STATE:
            # Draw zombies
            self.zombie_manager.draw(self.screen)
            
            # Draw UI
            accuracy = (self.hits / self.total_shots * 100) if self.total_shots > 0 else 0
            alive_zombie_count = self.zombie_manager.get_alive_count()
            self.ui.draw_game_ui(self.score, self.game_timer, accuracy, alive_zombie_count)
            
            # Draw crosshair
            mouse_pos = pygame.mouse.get_pos()
            crosshair_rect = self.crosshair_surface.get_rect(center=mouse_pos)
            self.screen.blit(self.crosshair_surface, crosshair_rect)
            
        elif self.state == GAME_OVER_STATE:
            accuracy = (self.hits / self.total_shots * 100) if self.total_shots > 0 else 0
            self.ui.draw_game_over(self.score, self.hits, self.total_shots, accuracy)
        
        # Update display
        pygame.display.flip()
