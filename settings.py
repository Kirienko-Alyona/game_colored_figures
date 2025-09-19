# settings.py

import pygame

# Розміри вікна
WIDTH, HEIGHT = 500, 500

# Більш м'які відтінки
BLACK = (20, 20, 20)           # Майже чорний, але менш різкий
WHITE = (240, 240, 240)        # Світло-сірий, не сліпучо-білий
GRAY = (180, 180, 180)         # Світлий сірий
# Кольори для кіл і квадрата
BLUE = (65, 105, 225)       # Royal Blue
YELLOW = (255, 204, 102)    # Mellow Yellow
PURPLE = (153, 50, 204)     # Dark Orchid
GREEN = (60, 179, 113)      # Medium Sea Green
COLORS = [BLUE, YELLOW, PURPLE, GREEN]

# Налаштування квадрата
SQUARE_SIZE = 50
SQUARE_SPEED = 10

# Налаштування кіл
CIRCLE_RADIUS = 20
CIRCLE_FALL_SPEED = 5
CIRCLE_SPAWN_TIME_RANGE = (100, 3000)  # мс

# Налаштування гри
FPS = 30
COLOR_CHANGE_TIME_RANGE = (5000, 10000)  # мс

# Шрифти перенесені в файл menu.py
# FONT = pygame.font.SysFont(None, 30)

FIGURES = {
    # CIRCLE: {},

}
