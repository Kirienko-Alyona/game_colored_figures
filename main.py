# main.py
import asyncio
import pygame
from states.gameplay import GameplayState
from states.menu import MenuState
from states.gameover import GameoverState
from states.level_select import LevelSelectState  # Новый импорт
from states.victory import VictoryState
from states.next_level import NextLevelState


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
        if state_name == 'menu':
            self.state = MenuState(
                self.screen, self.total_score, self.current_level, self)
        elif state_name == 'gameplay':
            self.state = GameplayState(self.screen, self, self.current_level)
        elif state_name == 'level_select':
            self.state = LevelSelectState(self.screen, self)

    def set_victory_state(self):
        self.state = VictoryState(
            self.screen, self.total_score, self.current_level, self)

    def set_next_level_state(self):
        self.state = NextLevelState(self.screen, self)

    def set_game_over_state(self):
        self.state = GameoverState(
            self.screen, self.total_score, self.current_level, self)

    def update_score_and_level(self, score):
        self.total_score += score
        self.current_level += 1

    def reset_game(self):
        self.total_score = 0
        self.current_level = 1

    async def run(self):
        running = True
        while running:
            self.state.handle_events()
            self.state.update()
            self.state.draw()
            pygame.display.update()
            self.clock.tick(30)
            await asyncio.sleep(0)  # важливо для Pygbag

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    asyncio.run(game.run())
