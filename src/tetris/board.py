class Board:
    def __init__(self, width=10, height=20):
        self.width = width
        self.height = height
        self.board = [[0 for i in range(width)] for j in range(height)]
        print(self.board)
    def printBoardText(self):
        for j in self.board[::-1]:
            for i in j:
                print(i, end="")
            print()