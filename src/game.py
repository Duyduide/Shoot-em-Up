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
        
        pygame.mouse.set_visible(True)
        
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
            # Load background image
            try:
                background_image = pygame.image.load(BACKGROUND_IMAGE).convert()
                
                self.background = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
                print("✅ Background image loaded successfully!")
            except Exception as bg_error:
                print(f"Warning: Could not load background image: {bg_error}")
                # Nào gặp lỗi thì vẽ tạm nền đen
                self.background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
                self.background.fill(BLACK)
            
            # Load crosshair image
            try:
                crosshair_original = pygame.image.load(CROSSHAIR_IMAGE).convert_alpha()

                self.crosshair_surface = pygame.transform.scale(crosshair_original, (32, 32))
                print("✅ Crosshair image loaded and scaled successfully!")
            except Exception as crosshair_error:
                print(f"Warning: Could not load crosshair image: {crosshair_error}")
                # Nào gặp lỗi thì vẽ tạm crosshair đơn giản
                self.crosshair_surface = pygame.Surface((32, 32), pygame.SRCALPHA)
                pygame.draw.circle(self.crosshair_surface, WHITE, (12, 12), 10, 2)
                pygame.draw.circle(self.crosshair_surface, WHITE, (12, 12), 1)
            
        except Exception as e:
            print(f"Warning: Could not load some assets: {e}")
    
    def run(self):
        """Main game loop"""
        while self.running:
            dt = self.clock.tick(FPS) / 1000.0  # Delta time in seconds
            
            self._handle_events()
            
            self._update(dt)
            
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

                        pygame.mouse.set_visible(True)
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
                elif event.key == pygame.K_RETURN:  # Enter key
                    if self.state == GAME_OVER_STATE:
                        self.state = MENU_STATE
                        pygame.mouse.set_visible(True)
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    self._handle_click(event.pos)
    
    def _handle_click(self, pos):
        """Handle mouse click"""
        if self.state == MENU_STATE:
            
            button_clicked = self.ui.handle_menu_click(pos)
            if button_clicked == "play":
                self._start_game()
            elif button_clicked == "quit":
                self.running = False
                
        elif self.state == PLAYING_STATE:
            
            self.total_shots += 1
            hit = self.zombie_manager.check_hit(pos)
            
            if hit:
                self.hits += 1
                self.score += HIT_POINTS
                self.sound_manager.play_hit()
            else:
                self.score += MISS_PENALTY
               
            
            self.sound_manager.play_shoot()
    
    def _start_game(self):
        """Start new game""" 
        self.state = PLAYING_STATE
        self.score = 0
        self.hits = 0
        self.total_shots = 0
        self.game_timer = GAME_DURATION
        self.zombie_manager.reset()
        self.zombie_manager.spawn_timer = 1.0        
        
        pygame.mouse.set_visible(False)
    
    def _update(self, dt):
        """Update game state"""
        if self.state == PLAYING_STATE:
            self.game_timer -= dt
            
            if self.game_timer <= 0:
                self.state = GAME_OVER_STATE
                
                pygame.mouse.set_visible(True)
                return
            
            self.zombie_manager.update(dt, self.game_timer)
    
    def _render(self):
        """Render game"""
        # Clear screen
        self.screen.blit(self.background, (0, 0))
        
        if self.state == MENU_STATE:
            self.ui.draw_menu()
            
        elif self.state == PLAYING_STATE:
            # Semi-transparent overlay
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            overlay.set_alpha(128)
            overlay.fill(BLACK)
            self.screen.blit(overlay, (0, 0))

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
