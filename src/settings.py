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
ZOMBIE_LIFETIME = 1.5  # 1.3 seconds per zombie
INITIAL_SPAWN_RATE = 2.0  # Initial spawn rate (seconds between spawns)
MIN_SPAWN_RATE = 0.5  # Minimum spawn rate (fastest spawning)

# Multi-spawn settings
MAX_ZOMBIES_ON_SCREEN = 3  # Maximum zombies on screen at once
MIN_ZOMBIES_PER_SPAWN = 1  # Minimum zombies to spawn at once
MAX_ZOMBIES_PER_SPAWN = 2  # Maximum zombies to spawn at once (early game)
LATE_GAME_MAX_SPAWN = 3    # Maximum zombies to spawn at once (late game)

# Cluster spawn settings
CLUSTER_RADIUS = 300       # Increased radius for larger zombies
MIN_CLUSTER_DISTANCE = 200  # Increased minimum distance for larger zombies
CLUSTER_CENTER_VARIATION = 30  # How close first zombie spawns to center

# Zombie settings
ZOMBIE_SMALL_SIZE = (150, 150)   # Increased from (32, 32)
ZOMBIE_LARGE_SIZE = (200, 200)   # Increased from (64, 64)
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

# Image files - Sprite Animation System
ZOMBIE_IDLE_IMAGES = [
    f"{IMAGES_DIR}/zombie-head--idle-1.png",     # Idle frame 1
    f"{IMAGES_DIR}/zombie-head-idle-2.png",      # Idle frame 2
    f"{IMAGES_DIR}/zombie head-idle-3.png.png",  # Idle frame 3
    f"{IMAGES_DIR}/zombie head-idle-4.png.png",  # Idle frame 4
    f"{IMAGES_DIR}/zombie-head-idle-5.png"       # Idle frame 5
]

ZOMBIE_HIT_IMAGES = [
    f"{IMAGES_DIR}/zombie head-hit-1.png.png",   # Hit frame 1
    f"{IMAGES_DIR}/zombie head-hit-2.png.png",   # Hit frame 2
    f"{IMAGES_DIR}/zombie head-hit-3.png.png",   # Hit frame 3
    f"{IMAGES_DIR}/zombie head-hit-4.png.png"    # Hit frame 4
]

BACKGROUND_IMAGE = f"{IMAGES_DIR}/background.png"
CROSSHAIR_IMAGE = f"{IMAGES_DIR}/crosshair.png"

# Animation settings
ZOMBIE_IDLE_ANIMATION_SPEED = 0.2    # Duration per idle frame (slower for breathing effect)
ZOMBIE_HIT_ANIMATION_DURATION = 0.4  # Duration of hit animation in seconds
ZOMBIE_HIT_FRAME_DURATION = 0.1      # Duration per hit frame

# Sound files
SHOOT_SOUND = f"{SOUNDS_DIR}/gun_shot.wav"
HIT_SOUND = f"{SOUNDS_DIR}/hit.wav"
THEME_MUSIC = f"{SOUNDS_DIR}/theme.wav"

# Game states
MENU_STATE = "menu"
PLAYING_STATE = "playing"
GAME_OVER_STATE = "game_over"
