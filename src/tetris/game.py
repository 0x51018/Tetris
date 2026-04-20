import pygame
from board import Board
from event import EventHandler
from draw import DrawManager

class Game:
    def __init__(self, BASE_DIR, width, height, fps=60):
        pygame.init()
        self.BASE_DIR = BASE_DIR
        self.screen = pygame.display.set_mode((width,height))
        self.clock = pygame.time.Clock()
        self.frame_rate = fps
        self.isGameRunning = True

        self.game_board = Board()
        self.event_handler = EventHandler(self.BASE_DIR)
        self.draw_manager = DrawManager(self.screen, self.game_board, width, height)

        print("Game instance initialized.")

    def run(self):
        print("Game.run() starting")
        while self.isGameRunning:
            """
            Real Loop Logic Part. begin
            """
            self.event_handler.check()
            self.draw_manager.draw()
            """
            end
            """
            self.clock.tick(self.frame_rate)
            pygame.display.flip()
        pygame.quit()