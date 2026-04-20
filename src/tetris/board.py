class Board:
    def __init__(self, width=10, height=23):
        self.width = width
        self.height = height
        # board start from bottom, left. board[0] is the lowest row.
        self.board = [[0 for col in range(self.width)] for row in range(self.height)]
        """
        TODO: need more rows for newly created minos. maybe exact 3 line. based of initial mino shape data.
        """

    # CLI printing board.
    def printBoardText(self):
        for j in self.board[::-1]:
            for i in j:
                print(i, end="")
            print()

    # return board for render & moving mino logics
    def getBoard(self):
        return self.board
    
    # remove full line and return how much lines had eliminated
    def remFullRows(self):
        full_rows = []
        for row in self.board:
            if min(row) > 0:
                full_rows.append(self.board.index(row))
        for i in full_rows:
            self.board.pop(i-full_rows.index(i))
        for j in range(len(full_rows)):
            self.board.append([0 for col in range(self.width)])
        return len(full_rows)
        # I'm not sure if it really works. need to test.