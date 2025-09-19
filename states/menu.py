# states/menu.py

import pygame
from settings import *
from levels import LEVEL_CONFIGS


class MenuState:
    def __init__(self, screen, total_score, current_level, game):
        self.screen = screen
        self.game = game

        self.total_score = total_score
        self.current_level = current_level
        self.total_levels = len(LEVEL_CONFIGS)

        self.font = pygame.font.SysFont(None, 40)
        self.font_small = pygame.font.SysFont(None, 30)

        # Кнопка "Грати"
        self.button_play_text = "Грати"
        self.button_play_color = GREEN
        self.button_play_rect = pygame.Rect(
            WIDTH // 2 - 75, HEIGHT // 2 + 50, 150, 50
        )

        # Кнопка "Обрати етап"
        self.button_select_text = "Обрати етап"
        self.button_select_color = BLUE
        self.button_select_rect = pygame.Rect(
            WIDTH // 2 - 100, HEIGHT // 2 + 120, 200, 50
        )

        # Кнопка "Почати гру заново"
        self.button_repeat_text = "Почати гру заново"
        self.button_repeat_color = GREEN
        self.button_repeat_rect = pygame.Rect(
            WIDTH // 2 - 125, HEIGHT // 2 + 120, 250, 50
        )

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.run = False
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.current_level <= self.total_levels:
                    if self.button_play_rect.collidepoint(event.pos):
                        self.game.set_state('gameplay')
                    if self.button_select_rect.collidepoint(event.pos):
                        self.game.set_state('level_select')
                else:
                    if self.button_repeat_rect.collidepoint(event.pos):
                        self.game.reset_game()
                        self.game.set_state('menu')

    def update(self):
        pass

    def draw(self):
        self.screen.fill(BLACK)

        title_text = self.font.render("Збирай кола!", True, WHITE)
        title_rect = title_text.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 - 100))
        self.screen.blit(title_text, title_rect)

        score_text = self.font_small.render(
            f"Загальний рахунок: {self.total_score}", True, WHITE)
        score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40))
        self.screen.blit(score_text, score_rect)

        level_text = self.font_small.render(
            f"Етап гри: {self.current_level}", True, WHITE)
        level_rect = level_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.screen.blit(level_text, level_rect)

        if self.current_level <= self.total_levels:
            # Рисуем кнопку "Грати"
            pygame.draw.rect(self.screen, self.button_play_color,
                             self.button_play_rect, border_radius=10)
            button_label = self.font_small.render(
                self.button_play_text, True, BLACK)
            button_label_rect = button_label.get_rect(
                center=self.button_play_rect.center)
            self.screen.blit(button_label, button_label_rect)

            # Рисуем кнопку "Обрати етап"
            pygame.draw.rect(self.screen, self.button_select_color,
                             self.button_select_rect, border_radius=10)
            button_select_label = self.font_small.render(
                self.button_select_text, True, WHITE)
            button_select_label_rect = button_select_label.get_rect(
                center=self.button_select_rect.center)
            self.screen.blit(button_select_label, button_select_label_rect)

        else:
            end_message = self.font_small.render(
                "Наступні етапи ще в розробці", True, WHITE)
            message_rect = end_message.get_rect(
                center=(WIDTH // 2, HEIGHT // 2 + 60))
            self.screen.blit(end_message, message_rect)

            pygame.draw.rect(self.screen, self.button_repeat_color,
                             self.button_repeat_rect, border_radius=10)
            button_label = self.font_small.render(
                self.button_repeat_text, True, BLACK)
            button_label_rect = button_label.get_rect(
                center=self.button_repeat_rect.center)
            self.screen.blit(button_label, button_label_rect)
