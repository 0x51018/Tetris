import pygame
from board import Board
from event import EventHandler

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

        print("Game instance initialized.")

    def run(self):
        print("Game.run() starting")
        while self.isGameRunning:
            """
            Real Loop Logic Part. begin
            """
            self.event_handler.check()
            """
            end
            """
            self.clock.tick(self.frame_rate)
            pygame.display.flip()
        pygame.quit()