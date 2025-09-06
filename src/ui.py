"""
SHOOT 'EM UP - UI Manager
Quản lý giao diện người dùng (menu, HUD, game over screen)
"""

import pygame
from .settings import *


class UI:
    """Class quản lý UI của game"""
    
    def __init__(self, screen):
        """Initialize UI"""
        self.screen = screen
        
        # Initialize fonts
        pygame.font.init()
        self.font_large = pygame.font.Font(None, FONT_SIZE_LARGE)
        self.font_medium = pygame.font.Font(None, FONT_SIZE_MEDIUM)
        self.font_small = pygame.font.Font(None, FONT_SIZE_SMALL)
        
        # Menu button rects
        self.play_button = pygame.Rect(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 - 50, 200, 50)
        self.quit_button = pygame.Rect(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 + 20, 200, 50)
    
    def draw_menu(self):
        """Draw main menu"""
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        # Title
        title_text = self.font_large.render("SHOOT 'EM UP", True, WHITE)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 150))
        self.screen.blit(title_text, title_rect)
        
        # Subtitle
        subtitle_text = self.font_medium.render("Click zombies before they disappear!", True, GRAY)
        subtitle_rect = subtitle_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 100))
        self.screen.blit(subtitle_text, subtitle_rect)
        
        # Play button
        pygame.draw.rect(self.screen, DARK_GRAY, self.play_button)
        pygame.draw.rect(self.screen, WHITE, self.play_button, 2)
        play_text = self.font_medium.render("PLAY", True, WHITE)
        play_rect = play_text.get_rect(center=self.play_button.center)
        self.screen.blit(play_text, play_rect)
        
        # Quit button
        pygame.draw.rect(self.screen, DARK_GRAY, self.quit_button)
        pygame.draw.rect(self.screen, WHITE, self.quit_button, 2)
        quit_text = self.font_medium.render("QUIT", True, WHITE)
        quit_rect = quit_text.get_rect(center=self.quit_button.center)
        self.screen.blit(quit_text, quit_rect)
        
        # Controls info
        controls_info = [
            "Controls:",
            "M - Mute/Unmute Music",
            "P - Pause/Resume Music",
            "ESC - Back/Quit"
        ]
        
        y_start = SCREEN_HEIGHT - 120
        for i, info in enumerate(controls_info):
            if i == 0:  # Title
                info_text = self.font_small.render(info, True, WHITE)
            else:  # Controls
                info_text = self.font_small.render(info, True, GRAY)
            
            info_rect = info_text.get_rect(center=(SCREEN_WIDTH//2, y_start + i * 25))
            self.screen.blit(info_text, info_rect)
    
    def handle_menu_click(self, pos):
        """Handle click on menu buttons"""
        if self.play_button.collidepoint(pos):
            return "play"
        elif self.quit_button.collidepoint(pos):
            return "quit"
        return None
    
    def draw_game_ui(self, score, time_left, accuracy, zombie_count=0):
        """Draw game UI (score, timer, accuracy, zombie count)"""
        # Score
        score_text = self.font_medium.render(f"Score: {score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        # Timer
        time_text = self.font_medium.render(f"Time: {time_left:.1f}s", True, WHITE)
        time_rect = time_text.get_rect()
        time_rect.topright = (SCREEN_WIDTH - 10, 10)
        self.screen.blit(time_text, time_rect)
        
        # Accuracy
        accuracy_text = self.font_small.render(f"Accuracy: {accuracy:.1f}%", True, WHITE)
        self.screen.blit(accuracy_text, (10, 50))
        
        # Zombie count (debug info)
        zombie_text = self.font_small.render(f"Zombies: {zombie_count}", True, GRAY)
        zombie_rect = zombie_text.get_rect()
        zombie_rect.topright = (SCREEN_WIDTH - 10, 50)
        self.screen.blit(zombie_text, zombie_rect)
    
    def draw_game_over(self, final_score, hits, total_shots, accuracy):
        """Draw game over screen"""
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        # Game Over title
        title_text = self.font_large.render("GAME OVER", True, WHITE)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 150))
        self.screen.blit(title_text, title_rect)
        
        # Stats
        stats = [
            f"Final Score: {final_score}",
            f"Hits: {hits}",
            f"Total Shots: {total_shots}",
            f"Accuracy: {accuracy:.1f}%"
        ]
        
        y_offset = SCREEN_HEIGHT//2 - 80
        for stat in stats:
            stat_text = self.font_medium.render(stat, True, WHITE)
            stat_rect = stat_text.get_rect(center=(SCREEN_WIDTH//2, y_offset))
            self.screen.blit(stat_text, stat_rect)
            y_offset += 40
        
        # Instructions
        instruction_text = self.font_small.render("Click anywhere to return to menu", True, GRAY)
        instruction_rect = instruction_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 100))
        self.screen.blit(instruction_text, instruction_rect)
