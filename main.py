# main.py

import pygame
from states.gameplay import GameplayState


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("Збирай кола того ж кольору, що квадрат")
        self.clock = pygame.time.Clock()
        self.state = GameplayState(self.screen)

    def run(self):
        running = True  # Створюємо змінну для керування циклом
        while running:
            # Обробка події закриття вікна
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False  # Змінюємо змінну на False, щоб вийти з циклу

            self.state.update()
            self.state.draw()
            pygame.display.update()
            self.clock.tick(30)

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
