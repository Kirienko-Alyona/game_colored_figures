# main.py

import pygame
from states.gameplay import GameplayState
from states.menu import MenuState


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("Збирай кола того ж кольору, що квадрат")
        self.clock = pygame.time.Clock()

        self.total_score = 0
        self.current_level = 1

        self.state = None
        self.set_state('menu')

    def set_state(self, state_name):
        # Коли ми переходимо в "gameplay" стан,
        # ми повинні створювати його НОВИЙ екземпляр щоразу
        if state_name == 'menu':
            self.state = MenuState(
                self.screen, self.total_score, self.current_level, self)
        elif state_name == 'gameplay':
            self.state = GameplayState(self.screen, self)

    def update_score_and_level(self, score):
        self.total_score += score
        self.current_level += 1

    def run(self):
        running = True
        while running:
            # Обробка подій, що впливають на стан
            self.state.handle_events()

            # Оновлення та малювання поточного стану
            self.state.update()
            self.state.draw()

            pygame.display.update()
            self.clock.tick(30)

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
