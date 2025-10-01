# sprites.py

import pygame
import random
from settings import *


class Square(pygame.sprite.Sprite):
    def __init__(self, x, y, size, color):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.color = color
        self.size = size

    def update(self, keys, width):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= SQUARE_SPEED
        if keys[pygame.K_RIGHT] and self.rect.right < width:
            self.rect.x += SQUARE_SPEED

    def change_color(self):
        self.color = random.choice(COLORS)
        self.image.fill(self.color)


class Circle(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, color):
        super().__init__()
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect(center=(x, y))
        self.color = color
        self.speed = CIRCLE_FALL_SPEED  # default

    def update(self):
        self.rect.y += self.speed


class Triangle(pygame.sprite.Sprite):
    def __init__(self, x, y, size, color):
        super().__init__()
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        points = [(size // 2, 0), (0, size), (size, size)]
        pygame.draw.polygon(self.image, color, points)
        self.rect = self.image.get_rect(center=(x, y))
        self.color = color
        self.size = size
        self.speed = CIRCLE_FALL_SPEED  # default

    def update(self):
        self.rect.y += self.speed
