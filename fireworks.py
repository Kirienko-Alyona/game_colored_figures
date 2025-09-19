# fireworks.py

import pygame
import random
from settings import *


class Firework(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.color = color
        self.size = random.randint(3, 8)
        self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        self.image.set_colorkey((0, 0, 0))

        # Малюємо коло, а не прямокутник
        pygame.draw.circle(self.image, self.color,
                           (self.size // 2, self.size // 2), self.size // 2)

        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = pygame.math.Vector2(
            random.uniform(-1.5, 1.5), random.uniform(-4, -8))
        self.alpha = 255
        self.fade_rate = random.randint(2, 5)

    def update(self):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y
        self.velocity.y += 0.2  # Додаємо гравітацію
        self.alpha -= self.fade_rate
        if self.alpha < 0:
            self.kill()

        # Змінюємо прозорість зображення
        self.image.set_alpha(self.alpha)
