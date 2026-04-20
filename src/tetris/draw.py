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
    def __init__(self, screen, width, height):
        self.screen = screen # screen 위에다가 그림을 그리는 방식임.
        self.width, self.hegith = width, height
        self.theme = 0 # 추후 theme의 index에 따라 이름 / 색 값들 받아올 수 있게 구현 예정. (언젠가)
        self.mino_colors = mino_colors
    
    def draw(self):
        # 화면을 그려야 함. 
        self.screen.fill((30,10,0))
        pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(100,100,100,100))