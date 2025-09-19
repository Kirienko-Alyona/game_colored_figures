# states/level_select.py

import pygame
from settings import *
from levels import LEVEL_CONFIGS


class LevelSelectState:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game
        self.total_levels = len(LEVEL_CONFIGS)

        self.font = pygame.font.SysFont(None, 40)
        self.font_small = pygame.font.SysFont(None, 24)

        self.buttons = []
        self.create_level_buttons()

    def create_level_buttons(self):
        button_size = 80
        spacing = 20
        start_x = (WIDTH - (self.total_levels * button_size +
                   (self.total_levels - 1) * spacing)) // 2
        start_y = HEIGHT // 2 - button_size // 2

        for i in range(1, self.total_levels + 1):
            button_rect = pygame.Rect(
                start_x, start_y, button_size, button_size)
            self.buttons.append({"rect": button_rect, "level": i})
            start_x += button_size + spacing

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Перевіряємо, чи натиснута кнопка "Назад"
                back_button_rect = pygame.Rect(20, 20, 100, 40)
                if back_button_rect.collidepoint(event.pos):
                    self.game.set_state('menu')
                    return

                for button in self.buttons:
                    if button["rect"].collidepoint(event.pos):
                        self.game.current_level = button["level"]
                        self.game.set_state('gameplay')

    def update(self):
        pass

    def draw(self):
        self.screen.fill(BLACK)

        title_text = self.font.render("Виберіть етап", True, WHITE)
        title_rect = title_text.get_rect(center=(WIDTH // 2, 80))
        self.screen.blit(title_text, title_rect)

        for button in self.buttons:
            pygame.draw.rect(self.screen, BLUE,
                             button["rect"], border_radius=10)
            level_text = self.font.render(str(button["level"]), True, WHITE)
            text_rect = level_text.get_rect(center=button["rect"].center)
            self.screen.blit(level_text, text_rect)

        # Кнопка "Назад"
        back_button_rect = pygame.Rect(20, 20, 100, 40)
        pygame.draw.rect(self.screen, GRAY, back_button_rect, border_radius=5)
        back_text = self.font_small.render("Назад", True, WHITE)
        back_text_rect = back_text.get_rect(center=back_button_rect.center)
        self.screen.blit(back_text, back_text_rect)
