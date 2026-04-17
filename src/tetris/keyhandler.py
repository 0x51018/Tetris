import pygame

class keyboardHandler:
    def __init__(self, key_dict):
        self.key_dict = key_dict
        self.key_status = {False for _ in range(len(self.key_dict))}
    def handle(self, key_constant, event_type):
        print("Recieved Key pressing event")
        
        pressed_func = self.key_dict[key_constant] # 어떤 동작인지 이름으로 받아오기.

        """
        TODO: 이제 동작 이름 : 함수 딕셔너리로 연결하거나 if 문으로 처리하거나 해서 동작을 연결하면 되는데
        문제는 변경할 board 상태랑 현재 drop 중인 블록 같은 상태들이 아직 아무데도 정의가 안 됐음.
        그걸 이제 board.py 안에서 정의해야 할 듯.
        - 보드 전체 상태 관리하는거
        - 이동이나 회전 시 벽 충돌 감지하는거 (이건 piece로 넘기는게 나으려나)
        - falling piece랑 holding piece, 완성된 board 관리하는거
        - 점수 체계나 통계?
        - 그리고 특정 주기마다 블록이 떨어지는거. 이런 것도 구현할 방식을 고안해야 함.
        """