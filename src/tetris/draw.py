import pygame
from board import Board

# mino colors acc
mino_colors = [
    (80, 80, 80),        # empty : black (or dark navy)
    (0, 255, 255),    # I mino : cyan
    (255, 255, 0),    # O mino : yellow
    (160, 0, 240),    # T mino : purple
    (0, 255, 0),      # S mino : green
    (255, 0, 0),      # Z mino : red
    (0, 0, 255),      # J mino : blue
    (255, 165, 0),    # L mino : orange
]



class DrawManager:
    def __init__(self, screen, board:Board, width, height):
        self.screen = screen # screen 위에다가 그림을 그리는 방식임.
        self.board_ref = board
        self.width, self.height = width, height # 픽셀 좌표 기반이기에 width/height에 대한 비율로 계산
        self.theme = 0 # 추후 theme의 index에 따라 이름 / 색 값들 받아올 수 있게 구현 예정. (언젠가)
        self.mino_colors = mino_colors
    
    def draw(self):
        # 화면을 그려야 함.
        board_height, board_width = self.height * 0.84, self.height * 0.4
        board_top, board_left = self.height * 0.1, (self.width - board_width)//2
        
        board_state = self.board_ref.getBoard()[::-1]
        tile_len = board_width//10

        self.screen.fill((4, 0, 43))
        pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(board_left, board_top, board_width, board_height))
        for i in range(len(board_state)):
            row = board_state[i]
            for j in range(len(row)):
                tile_top, tile_left = board_top + (20-i) * tile_len, board_left + j * tile_len
                color_value = row[j]
                pygame.draw.rect(self.screen, mino_colors[color_value], pygame.Rect(tile_left+1, tile_top+1, tile_len-2, tile_len-2))
                # 나누었을 때 정수가 되지 않는 문제때문에 픽셀 매치가 정확히 되지 않고 있음. 
                # 모든 좌표 계산시 나누기를 다시 하면 해결되고, 혹은 화면 사이즈에 맞게 정확한 픽셀 수로 고정하면 되긴 한데
                # 다른 방법은 없을까?