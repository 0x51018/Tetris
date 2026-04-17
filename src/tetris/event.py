import pygame
import json
from pathlib import Path
from keyhandler import keyboardHandler

class EventHandler:
    def __init__(self, BASE_DIR):
        print("EventHandler initializing")
        self.keys_check = [] # 조작법에 포함되는 키들 저장하는 List
        self.CONFIG_DIR = BASE_DIR / 'config.json'
        self.key_dict = self.load_control_keys()
        self.key_handler = keyboardHandler(self.key_dict)

        self.isKeyPossible = pygame.key.get_focused
        if self.isKeyPossible == False: print("현재 키보드 입력을 감지할 수 없는 상태입니다.")

    def load_control_keys(self):
        with self.CONFIG_DIR.open() as f:
            control_data = (json.load(f))['control']
        print(control_data)
        result = {
                    getattr(pygame, key): action 
                    for action, keys in control_data.items() 
                    for key in keys 
                }
        return result

    # 매 프레임마다 실행하는 이벤트 확인용 메서드.
    def check(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if event.key in self.key_dict.keys():
                    self.key_handler.handle(event.key, event.type)
                print("Oh there is key pressing event!")