#!/usr/bin/env python3
"""
SHOOT 'EM UP - Game Entry Point
Main file để khởi chạy game
"""

import sys
import pygame
from src.game import Game

def main():
    """Main function để khởi chạy game"""
    try:
        # Khởi tạo Pygame
        pygame.init()
        
        # Tạo và chạy game
        game = Game()
        game.run()
        
        # Stop background music when game ends
        game.sound_manager.stop_theme_music()
        
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    finally:
        # Cleanup
        pygame.mixer.quit()
        pygame.quit()
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
