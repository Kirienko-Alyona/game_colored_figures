# states/next_level.py

import pygame
from settings import *
from levels import LEVEL_CONFIGS


class NextLevelState:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game
        self.current_level = self.game.current_level

        # Перевіряємо, чи існує наступний рівень
        self.next_level_config = LEVEL_CONFIGS.get(self.current_level)

        self.font = pygame.font.SysFont(None, 40)
        self.font_small = pygame.font.SysFont(None, 24)

        # Кнопка "Грати" (для початку наступного етапу)
        self.play_button_text = "Грати"
        self.play_button_color = GREEN
        self.play_button_rect = pygame.Rect(
            WIDTH // 2 - 75, HEIGHT // 2 + 70, 150, 50
        )

        # Кнопка "Повернутись до меню"
        self.menu_button_text = "Повернутись до меню"
        self.menu_button_color = GREEN
        self.menu_button_rect = pygame.Rect(
            WIDTH // 2 - 150, HEIGHT // 2 + 150, 300, 50
        )

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.menu_button_rect.collidepoint(event.pos):
                    self.game.set_state('menu')
                if self.play_button_rect.collidepoint(event.pos):
                    self.game.set_state('gameplay')

    def update(self):
        pass

    def draw(self):
        self.screen.fill(BLACK)

        # Заголовок етапу
        if self.next_level_config:
            title_text = self.font.render(
                f"Етап {self.current_level}: {self.next_level_config['name']}", True, WHITE)
            title_rect = title_text.get_rect(
                center=(WIDTH // 2, HEIGHT // 2 - 100))
            self.screen.blit(title_text, title_rect)

            # Опис завдання
            desc_text = self.font_small.render(
                self.next_level_config['description'], True, WHITE)
            desc_rect = desc_text.get_rect(
                center=(WIDTH // 2, HEIGHT // 2 - 40))
            self.screen.blit(desc_text, desc_rect)

            # Загальний рахунок
            score_text = self.font_small.render(
                f"Загальний рахунок: {self.game.total_score}", True, WHITE)
            score_rect = score_text.get_rect(
                center=(WIDTH // 2, HEIGHT // 2 + 20))
            self.screen.blit(score_text, score_rect)

            # Кнопка "Грати"
            play_button_color = self.play_button_color
            if self.play_button_rect.collidepoint(pygame.mouse.get_pos()):
                play_button_color = LIGHT_GRAY

            pygame.draw.rect(self.screen, play_button_color,
                             self.play_button_rect, border_radius=10)
            button_label = self.font_small.render(
                self.play_button_text, True, BLACK)
            button_label_rect = button_label.get_rect(
                center=self.play_button_rect.center)
            self.screen.blit(button_label, button_label_rect)
        else:
            # Якщо етапу немає в levels.py
            message_text = self.font.render(
                "Наступні етапи ще в розробці", True, WHITE)
            message_rect = message_text.get_rect(
                center=(WIDTH // 2, HEIGHT // 2 - 50))
            self.screen.blit(message_text, message_rect)

        # Кнопка "Повернутись до меню"
        menu_button_color = self.menu_button_color
        if self.menu_button_rect.collidepoint(pygame.mouse.get_pos()):
            menu_button_color = LIGHT_GRAY

        pygame.draw.rect(self.screen, menu_button_color,
                         self.menu_button_rect, border_radius=10)
        button_label = self.font_small.render(
            self.menu_button_text, True, WHITE)
        button_label_rect = button_label.get_rect(
            center=self.menu_button_rect.center)
        self.screen.blit(button_label, button_label_rect)
