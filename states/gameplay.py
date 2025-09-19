# states/gameplay.py

import pygame
import random
from settings import *
from sprites import Square, Circle
from levels import LEVEL_CONFIGS


class GameplayState:
    def __init__(self, screen, game, current_level):
        self.screen = screen
        self.game = game
        self.current_level = current_level
        self.score = 0

        # Завантаження конфігурації для поточного рівня
        self.level_config = LEVEL_CONFIGS.get(
            self.current_level, LEVEL_CONFIGS[1])

        self.font = pygame.font.SysFont(None, 30)

        # Встановлення кольору квадрата з конфігурації
        square_color = self.level_config["square_color"]
        if square_color == "random":
            square_color = random.choice(COLORS)

        self.square = Square(
            WIDTH // 2 - SQUARE_SIZE // 2,
            HEIGHT - SQUARE_SIZE - 10,
            SQUARE_SIZE,
            square_color
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

        # Визначаємо, чи є коло, що знаходиться в зоні квадратика
        circle_in_danger_zone = False
        for circle in self.circles:
            # Змінено: зона небезпеки тепер 3 висоти квадрата від його нижнього краю
            if circle.rect.bottom >= self.square.rect.bottom - (3 * self.square.size):
                circle_in_danger_zone = True
                break

        # Логіка зміни кольору (якщо дозволено конфігурацією і немає кола в небезпечній зоні)
        if self.level_config["change_square_color"] and not circle_in_danger_zone:
            if current_time >= self.next_color_change_time:
                self.square.change_color()
                self.next_color_change_time = current_time + \
                    random.randint(*COLOR_CHANGE_TIME_RANGE)

        # Логіка появи кіл
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

        keys = pygame.key.get_pressed()
        self.square.update(keys, WIDTH)

        # Оновлення швидкості падіння кіл з конфігурації рівня
        for circle in self.circles:
            circle.rect.y += self.level_config["circle_speed"]

        # Обробка зіткнень
        collided_circles = pygame.sprite.spritecollide(
            self.square, self.circles, False)
        for circle in collided_circles:
            if circle.color == self.square.color:
                self.score += 1
                circle.kill()
            else:
                self.game.set_game_over_state()

        # Перевірка на умову перемоги після кожного оновлення
        if self.score >= self.level_config["win_score"]:
            self.game.update_score_and_level(self.score)
            self.game.set_state('menu')

        # Обробка кіл, які вилетіли за екран
        for circle in list(self.circles):
            if circle.rect.top > HEIGHT:
                if circle.color == self.square.color:
                    self.score -= 1
                circle.kill()

    def draw(self):
        self.screen.fill(BLACK)

        self.screen.blit(self.square.image, self.square.rect)
        self.circles.draw(self.screen)

        score_text = self.font.render(str(self.score), True, WHITE)
        text_rect = score_text.get_rect(
            center=(self.square.rect.centerx, self.square.rect.centery)
        )
        self.screen.blit(score_text, text_rect)
