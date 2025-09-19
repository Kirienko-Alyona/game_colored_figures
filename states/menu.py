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

        # Новий код: Кнопка "Вийти з гри" в основному меню
        self.button_exit_text = "Вийти з гри"
        self.button_exit_color = RED
        self.button_exit_rect = pygame.Rect(
            WIDTH // 2 - 75, HEIGHT // 2 + 190, 150, 50
        )

        # Кнопка "Почати гру заново"
        self.button_repeat_text = "Почати гру заново"
        self.button_repeat_color = GREEN
        self.button_repeat_rect = pygame.Rect(
            WIDTH // 2 - 125, HEIGHT // 2 + 120, 250, 50
        )

        # Новий код: Кнопка "Вийти з гри" на екрані закінчення гри
        self.button_exit_gameover_text = "Вийти з гри"
        self.button_exit_gameover_color = RED
        self.button_exit_gameover_rect = pygame.Rect(
            WIDTH // 2 - 125, HEIGHT // 2 + 180, 250, 50
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
                        self.game.set_next_level_state()
                    if self.button_select_rect.collidepoint(event.pos):
                        self.game.set_state('level_select')
                    # Новий код: Обробка натискання кнопки виходу в основному меню
                    if self.button_exit_rect.collidepoint(event.pos):
                        pygame.quit()
                        exit()
                else:
                    if self.button_repeat_rect.collidepoint(event.pos):
                        self.game.reset_game()
                        self.game.set_state('menu')
                    # Новий код: Обробка натискання кнопки виходу на екрані закінчення гри
                    if self.button_exit_gameover_rect.collidepoint(event.pos):
                        pygame.quit()
                        exit()

    def update(self):
        pass

    def draw(self):
        self.screen.fill(BLACK)
        title_text = self.font.render("Збирай кола!", True, WHITE)
        title_rect = title_text.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 - 100))
        self.screen.blit(title_text, title_rect)

        if self.current_level <= self.total_levels:
            score_text = self.font_small.render(
                f"Загальний рахунок: {self.total_score}", True, WHITE)
            score_rect = score_text.get_rect(
                center=(WIDTH // 2, HEIGHT // 2 - 40))
            self.screen.blit(score_text, score_rect)

            # Кнопка "Грати"
            play_color = self.button_play_color
            if self.button_play_rect.collidepoint(pygame.mouse.get_pos()):
                play_color = LIGHT_GRAY
            pygame.draw.rect(self.screen, play_color,
                             self.button_play_rect, border_radius=10)
            button_label = self.font_small.render(
                self.button_play_text, True, BLACK)
            button_label_rect = button_label.get_rect(
                center=self.button_play_rect.center)
            self.screen.blit(button_label, button_label_rect)

            # Кнопка "Обрати етап"
            select_color = self.button_select_color
            if self.button_select_rect.collidepoint(pygame.mouse.get_pos()):
                select_color = LIGHT_GRAY
            pygame.draw.rect(self.screen, select_color,
                             self.button_select_rect, border_radius=10)
            button_select_label = self.font_small.render(
                self.button_select_text, True, WHITE)
            button_select_label_rect = button_select_label.get_rect(
                center=self.button_select_rect.center)
            self.screen.blit(button_select_label, button_select_label_rect)

            # Новий код: Кнопка "Вийти з гри" в основному меню
            exit_color = self.button_exit_color
            if self.button_exit_rect.collidepoint(pygame.mouse.get_pos()):
                exit_color = LIGHT_GRAY
            pygame.draw.rect(self.screen, exit_color,
                             self.button_exit_rect, border_radius=10)
            button_exit_label = self.font_small.render(
                self.button_exit_text, True, WHITE)
            button_exit_label_rect = button_exit_label.get_rect(
                center=self.button_exit_rect.center)
            self.screen.blit(button_exit_label, button_exit_label_rect)

        else:
            # Оновлено: екран "в розробці"
            end_message = self.font_small.render(
                "Наступні етапи ще в розробці", True, WHITE)
            message_rect = end_message.get_rect(
                center=(WIDTH // 2, HEIGHT // 2 - 40))
            self.screen.blit(end_message, message_rect)

            # Кнопка "Почати гру заново"
            repeat_color = self.button_repeat_color
            if self.button_repeat_rect.collidepoint(pygame.mouse.get_pos()):
                repeat_color = LIGHT_GRAY
            pygame.draw.rect(self.screen, repeat_color,
                             self.button_repeat_rect, border_radius=10)
            button_label = self.font_small.render(
                self.button_repeat_text, True, BLACK)
            button_label_rect = button_label.get_rect(
                center=self.button_repeat_rect.center)
            self.screen.blit(button_label, button_label_rect)

            # Новий код: Кнопка "Вийти з гри" на екрані закінчення гри
            exit_gameover_color = self.button_exit_gameover_color
            if self.button_exit_gameover_rect.collidepoint(pygame.mouse.get_pos()):
                exit_gameover_color = LIGHT_GRAY
            pygame.draw.rect(self.screen, exit_gameover_color,
                             self.button_exit_gameover_rect, border_radius=10)
            button_exit_gameover_label = self.font_small.render(
                self.button_exit_gameover_text, True, WHITE)
            button_exit_gameover_label_rect = button_exit_gameover_label.get_rect(
                center=self.button_exit_gameover_rect.center)
            self.screen.blit(button_exit_gameover_label,
                             button_exit_gameover_label_rect)
