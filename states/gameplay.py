# states/gameplay.py

import pygame
import random
from settings import *
from sprites import Square, Circle, Triangle
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

        self.figure_types = self.level_config.get(
            "figure_type", [Circle, Triangle])

        self.required_figures = self.level_config.get(
            "required_figures", {"Circle": 3})
        self.collected = {k: 0 for k in self.required_figures}

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
        self.falling_figures = pygame.sprite.Group()

        self.next_spawn_time = pygame.time.get_ticks(
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

        # Визначаємо, чи є фігура, що знаходиться в зоні квадратика
        figure_in_danger_zone = False
        for figure in self.falling_figures:
            # Змінено: зона небезпеки тепер 3 висоти квадрата від його нижнього краю
            if figure.rect.bottom >= self.square.rect.bottom - (3 * self.square.size):
                figure_in_danger_zone = True
                break

        # Логіка зміни кольору (якщо дозволено конфігурацією і немає фігури в небезпечній зоні)
        if self.level_config["change_square_color"] and not figure_in_danger_zone:
            if current_time >= self.next_color_change_time:
                self.square.change_color()
                self.next_color_change_time = current_time + \
                    random.randint(*COLOR_CHANGE_TIME_RANGE)

        # Логіка появи фігур
        if current_time >= self.next_spawn_time:
            FigureClass = random.choice(self.figure_types)
            color = random.choice(COLORS)
            speed = self.level_config.get("circle_speed", 5)
            if FigureClass == Circle:
                radius = CIRCLE_RADIUS
                x = random.randint(radius, WIDTH - radius)
                y = -radius
                figure = FigureClass(x, y, radius, color)
                figure.speed = speed
            elif FigureClass == Triangle:
                size = 40
                x = random.randint(size // 2, WIDTH - size // 2)
                y = -size
                figure = FigureClass(x, y, size, color)
                figure.speed = speed
            else:
                # Fallback only if unexpected class
                figure = Circle(random.randint(
                    CIRCLE_RADIUS, WIDTH - CIRCLE_RADIUS), -CIRCLE_RADIUS, CIRCLE_RADIUS, color)
                figure.speed = speed
            self.falling_figures.add(figure)
            self.next_spawn_time = current_time + \
                random.randint(*CIRCLE_SPAWN_TIME_RANGE)

        keys = pygame.key.get_pressed()
        self.square.update(keys, WIDTH)

        # Оновлення фігур - викликаємо update() замість ручного додавання швидкості
        for figure in self.falling_figures:
            figure.update()

        # Обробка зіткнень
        collided_figures = pygame.sprite.spritecollide(
            self.square, self.falling_figures, False)
        for figure in collided_figures:
            figure_type = type(figure).__name__
            if figure.color == self.square.color and figure_type in self.collected:
                self.collected[figure_type] += 1
                figure.kill()
            else:
                self.game.set_game_over_state()

        # Перехід на екран перемоги
        if all(self.collected[k] >= v for k, v in self.required_figures.items()):
            total_score = sum(self.collected.values())
            self.game.update_score_and_level(total_score)
            self.game.set_victory_state()

        # Обробка фігур, які вилетіли за екран
        for figure in list(self.falling_figures):
            if figure.rect.top > HEIGHT:
                figure_type = type(figure).__name__
                if figure.color == self.square.color and figure_type in self.collected:
                    self.collected[figure_type] = max(
                        0, self.collected[figure_type] - 1)
                figure.kill()

    def draw(self):
        self.screen.fill(BLACK)

        self.screen.blit(self.square.image, self.square.rect)
        self.falling_figures.draw(self.screen)

        score_text = self.font.render(
            str(sum(self.collected.values())), True, WHITE)
        text_rect = score_text.get_rect(
            center=(self.square.rect.centerx, self.square.rect.centery)
        )
        self.screen.blit(score_text, text_rect)
