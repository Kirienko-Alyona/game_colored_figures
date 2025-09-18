# states/gameplay.py

import pygame
import random
from settings import *
from sprites import Square, Circle


class GameplayState:
    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.font = pygame.font.SysFont(None, 30)

        self.square = Square(
            WIDTH // 2 - SQUARE_SIZE // 2,
            HEIGHT - SQUARE_SIZE - 10,
            SQUARE_SIZE,
            random.choice(COLORS)
        )
        self.circles = pygame.sprite.Group()

        self.next_circle_time = pygame.time.get_ticks(
        ) + random.randint(*CIRCLE_SPAWN_TIME_RANGE)
        self.next_color_change_time = pygame.time.get_ticks() + random.randint(*
                                                                               COLOR_CHANGE_TIME_RANGE)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def update(self):
        current_time = pygame.time.get_ticks()

        # Оновлення кольору квадрата
        if current_time >= self.next_color_change_time:
            self.square.change_color()
            self.next_color_change_time = current_time + \
                random.randint(*COLOR_CHANGE_TIME_RANGE)

        # Створення нового кола
        if current_time >= self.next_circle_time:
            self.circles.add(
                Circle(
                    random.randint(CIRCLE_RADIUS, WIDTH - CIRCLE_RADIUS),
                    -CIRCLE_RADIUS,
                    CIRCLE_RADIUS,
                    random.choice(COLORS)
                )
            )
            self.next_circle_time = current_time + \
                random.randint(*CIRCLE_SPAWN_TIME_RANGE)

        # Оновлення спрайтів
        keys = pygame.key.get_pressed()
        self.square.update(keys, WIDTH)
        self.circles.update()

        # Перевірка зіткнень
        collided_circles = pygame.sprite.spritecollide(
            self.square, self.circles, False)
        for circle in collided_circles:
            if circle.color == self.square.color:
                self.score += 1
                circle.kill()
            else:
                print("Гра закінчена! Ваш рахунок:", self.score)
                pygame.quit()
                exit()

        # Видалення кіл, що впали
        for circle in list(self.circles):
            if circle.rect.top > HEIGHT:
                if circle.color == self.square.color:
                    self.score -= 1
                circle.kill()

    def draw(self):
        self.screen.fill(BLACK)

        self.screen.blit(self.square.image, self.square.rect)
        self.circles.draw(self.screen)

        # Відображення рахунку
        score_text = self.font.render(str(self.score), True, WHITE)
        text_rect = score_text.get_rect(
            center=(self.square.rect.centerx, self.square.rect.centery)
        )
        self.screen.blit(score_text, text_rect)
