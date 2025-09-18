# states/gameover.py

import pygame
from settings import *


class GameoverState:
    def __init__(self, screen, total_score, current_level, game):
        self.screen = screen
        self.game = game

        self.total_score = total_score
        self.current_level = current_level

        self.font = pygame.font.SysFont(None, 40)
        self.font_small = pygame.font.SysFont(None, 30)

        self.button_text = "Пройти етап знову"
        self.button_color = BLUE
        self.button_rect = pygame.Rect(
            WIDTH // 2 - 125, HEIGHT // 2 + 50, 250, 50
        )

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.run = False
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.button_rect.collidepoint(event.pos):
                    # Починаємо знову з поточного етапу
                    self.game.set_state('gameplay')

    def update(self):
        pass

    def draw(self):
        self.screen.fill(BLACK)

        # Заголовок "Завдання не виконано"
        title_text = self.font.render("Завдання не виконано", True, WHITE)
        title_rect = title_text.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 - 100))
        self.screen.blit(title_text, title_rect)

        # Інформація про рахунок та етап
        score_text = self.font_small.render(
            f"Загальний рахунок: {self.total_score}", True, WHITE)
        score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40))
        self.screen.blit(score_text, score_rect)

        level_text = self.font_small.render(
            f"Етап гри: {self.current_level}", True, WHITE)
        level_rect = level_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.screen.blit(level_text, level_rect)

        # Кнопка "Пройти етап знову"
        pygame.draw.rect(self.screen, self.button_color,
                         self.button_rect, border_radius=10)
        button_label = self.font_small.render(self.button_text, True, WHITE)
        button_label_rect = button_label.get_rect(
            center=self.button_rect.center)
        self.screen.blit(button_label, button_label_rect)
