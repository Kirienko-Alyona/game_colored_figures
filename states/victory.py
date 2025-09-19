# states/victory.py
import random
import pygame
from settings import *
from fireworks import Firework  # Впевнися, що ти імпортуєш клас Firework


class VictoryState:
    def __init__(self, screen, total_score, current_level, game):
        self.screen = screen
        self.game = game
        self.total_score = total_score
        self.current_level = current_level
        self.font_large = pygame.font.SysFont(None, 60)
        self.font_small = pygame.font.SysFont(None, 30)

        # Кнопка "Наступний етап"
        self.next_button_text = "Наступний етап"
        self.next_button_color = GREEN
        self.next_button_rect = pygame.Rect(
            WIDTH // 2 - 125, HEIGHT // 2 + 50, 250, 50
        )

        self.fireworks = pygame.sprite.Group()
        self.last_firework_time = pygame.time.get_ticks()
        self.firework_spawn_rate = 500  # Мілісекунди між салютами

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.next_button_rect.collidepoint(event.pos):
                    self.game.set_next_level_state()

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_firework_time > self.firework_spawn_rate:
            # Запускаємо новий салют
            for _ in range(30):  # 30 частинок для одного салюту
                self.fireworks.add(
                    Firework(
                        random.choice(COLORS),
                        random.randint(0, WIDTH),
                        HEIGHT
                    )
                )
            self.last_firework_time = current_time

        self.fireworks.update()

    def draw(self):
        self.screen.fill(BLACK)

        # Напис "Етап пройдено!"
        title_text = self.font_large.render("Етап пройдено!", True, WHITE)
        title_rect = title_text.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 - 100))
        self.screen.blit(title_text, title_rect)

        # Інформація про загальний рахунок
        score_text = self.font_small.render(
            f"Загальний рахунок: {self.total_score}", True, WHITE)
        score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40))
        self.screen.blit(score_text, score_rect)

        # Відображаємо салют
        self.fireworks.draw(self.screen)

        # Кнопка "Наступний етап"
        next_level_color = GREEN
        if self.next_button_rect.collidepoint(pygame.mouse.get_pos()):
            next_level_color = LIGHT_GRAY

        pygame.draw.rect(self.screen, next_level_color,
                         self.next_button_rect, border_radius=10)
        button_label = self.font_small.render(
            self.next_button_text, True, BLACK)
        button_label_rect = button_label.get_rect(
            center=self.next_button_rect.center)
        self.screen.blit(button_label, button_label_rect)
