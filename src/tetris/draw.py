import pygame

mino_colors = [
    (0, 255, 255),    # I mino : cyan
    (255, 255, 0),    # O mino : yellow
    (160, 0, 240),    # T mino : purple
    (0, 255, 0),      # S mino : green
    (255, 0, 0),      # Z mino : red
    (0, 0, 255),      # J mino : blue
    (255, 165, 0),    # L mino : orange
]

class DrawManager:
    def __init__(self, width, height):
        self.theme = 0 # 추후 theme의 index에 따라 이름 / 색 값들 받아올 수 있게 구현 예정. (언젠가)
        self.mino_colors = mino_colors
    
    def draw(self):
        pygame.draw.rect()
        # 화면을 그려야 함. 