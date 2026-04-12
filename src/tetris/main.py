import pygame
from game import Game 

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
isGameRunning = True

main_game = Game()
main_game.game_board.printBoardText()
pygame.quit()