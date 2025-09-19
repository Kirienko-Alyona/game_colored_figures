# settings.py

import pygame

# Розміри вікна
WIDTH, HEIGHT = 500, 500

# Кольори
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
COLORS = [BLUE, YELLOW, PURPLE, GREEN]

# Налаштування квадрата
SQUARE_SIZE = 50
SQUARE_SPEED = 10

# Налаштування кіл
CIRCLE_RADIUS = 20
CIRCLE_FALL_SPEED = 5
CIRCLE_SPAWN_TIME_RANGE = (1000, 3000)  # мс

# Налаштування гри
FPS = 30
COLOR_CHANGE_TIME_RANGE = (5000, 10000)  # мс

# Шрифти
# FONT = pygame.font.SysFont(None, 30)
