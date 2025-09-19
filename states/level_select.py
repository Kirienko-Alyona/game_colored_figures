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
        button_size = 50
        spacing = 20
        buttons_per_row = 6

        # Розрахунок стартових позицій для першого рядка
        row_width = buttons_per_row * button_size + \
            (buttons_per_row - 1) * spacing
        start_x = (WIDTH - row_width) // 2
        start_y = HEIGHT // 2 - button_size * 2  # Відступи для кількох рядків

        for i in range(1, self.total_levels + 1):
            row = (i - 1) // buttons_per_row
            col = (i - 1) % buttons_per_row

            x = start_x + col * (button_size + spacing)
            y = start_y + row * (button_size + spacing)

            button_rect = pygame.Rect(x, y, button_size, button_size)
            self.buttons.append({"rect": button_rect, "level": i})

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
                        self.game.set_next_level_state()

    def update(self):
        pass

    def draw(self):
        self.screen.fill(BLACK)

        title_text = self.font.render("Виберіть етап", True, WHITE)
        title_rect = title_text.get_rect(center=(WIDTH // 2, 80))
        self.screen.blit(title_text, title_rect)

        for button in self.buttons:
            # Визначаємо колір кнопки етапу залежно від положення курсору
            button_color = BLUE
            if button["rect"].collidepoint(pygame.mouse.get_pos()):
                button_color = LIGHT_GRAY

            pygame.draw.rect(self.screen, button_color,
                             button["rect"], border_radius=10)
            level_text = self.font.render(str(button["level"]), True, WHITE)
            text_rect = level_text.get_rect(center=button["rect"].center)
            self.screen.blit(level_text, text_rect)

        # Кнопка "Назад"
        back_button_rect = pygame.Rect(20, 20, 100, 40)

        # Визначаємо колір кнопки "Назад" залежно від положення курсору
        back_color = GRAY
        if back_button_rect.collidepoint(pygame.mouse.get_pos()):
            back_color = LIGHT_GRAY

        pygame.draw.rect(self.screen, back_color,
                         back_button_rect, border_radius=5)
        back_text = self.font_small.render("Назад", True, WHITE)
        back_text_rect = back_text.get_rect(center=back_button_rect.center)
        self.screen.blit(back_text, back_text_rect)
