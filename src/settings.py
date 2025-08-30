"""
SHOOT 'EM UP - Game Settings
Chứa tất cả constants và cấu hình của game
"""

import pygame

# Screen settings
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
FPS = 60

# Colors (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
DARK_GRAY = (64, 64, 64)

# Game settings
GAME_DURATION = 30  # 30 seconds per round
ZOMBIE_LIFETIME = 1.3  # 1.3 seconds per zombie
INITIAL_SPAWN_RATE = 2.0  # Initial spawn rate (seconds between spawns)
MIN_SPAWN_RATE = 0.5  # Minimum spawn rate (fastest spawning)

# Zombie settings
ZOMBIE_SMALL_SIZE = (32, 32)
ZOMBIE_LARGE_SIZE = (64, 64)
ZOMBIE_SPAWN_MARGIN = 50  # Margin from screen edges

# Scoring
HIT_POINTS = 10
MISS_PENALTY = -2  # Set to 0 if no penalty needed

# Font settings
FONT_SIZE_LARGE = 48
FONT_SIZE_MEDIUM = 32
FONT_SIZE_SMALL = 24

# Asset paths
ASSETS_DIR = "assets"
IMAGES_DIR = f"{ASSETS_DIR}/images"
SOUNDS_DIR = f"{ASSETS_DIR}/sounds"

# Image files
ZOMBIE_SMALL_IMAGE = f"{IMAGES_DIR}/zombie_small.png"
ZOMBIE_LARGE_IMAGE = f"{IMAGES_DIR}/zombie_large.png"
BACKGROUND_IMAGE = f"{IMAGES_DIR}/background.png"
CROSSHAIR_IMAGE = f"{IMAGES_DIR}/crosshair.png"

# Sound files
SHOOT_SOUND = f"{SOUNDS_DIR}/shoot.wav"
HIT_SOUND = f"{SOUNDS_DIR}/hit.wav"
MISS_SOUND = f"{SOUNDS_DIR}/miss.wav"

# Game states
MENU_STATE = "menu"
PLAYING_STATE = "playing"
GAME_OVER_STATE = "game_over"
