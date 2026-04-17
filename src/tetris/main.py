from game import Game
from pathlib import Path

def main():
    BASE_DIR = Path(__file__).resolve().parent
    main_game = Game(BASE_DIR, 1280, 720)
    main_game.run()

if __name__ == "__main__":
    main()