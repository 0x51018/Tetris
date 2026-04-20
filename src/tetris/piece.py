mino_types = [None, "I", "S", "Z", "T", "L", "J", "O"]
mino_shapes = {
    "I":[
            [[0,0,0,0],[1,1,1,1],[0,0,0,0],[0,0,0,0]], 
            [[0,0,1,0],[0,0,1,0],[0,0,1,0],[0,0,1,0]], 
            [[0,0,0,0],[0,0,0,0],[1,1,1,1],[0,0,0,0]], 
            [[0,1,0,0],[0,1,0,0],[0,1,0,0],[0,1,0,0]]
        ],
    "S":[
            [[0,1,1],[1,1,0],[0,0,0]],
            [[0,1,0],[0,1,1],[0,0,1]],
            [[0,0,0],[0,1,1],[1,1,0]],
            [[1,0,0],[1,1,0],[0,1,0]]
        ],
    "Z":[
            [[1,1,0],[0,1,1],[0,0,0]],
            [[0,0,1],[0,1,1],[0,1,0]],
            [[0,0,0],[0,1,1],[1,1,0]],
            [[0,1,0],[1,1,0],[1,0,0]]
        ],
    "T":[
            [[0,1,0],[1,1,1],[0,0,0]],
            [[0,1,0],[0,1,1],[0,1,0]],
            [[0,0,0],[1,1,1],[0,1,0]],
            [[0,1,0],[1,1,0],[0,1,0]]
        ],
    "L":[
            [[0,0,1],[1,1,1],[0,0,0]],
            [[0,1,0],[0,1,0],[0,1,1]],
            [[0,0,0],[1,1,1],[1,0,0]],
            [[1,1,0],[0,1,0],[0,1,0]]
        ],
    "J":[
            [[1,0,0],[1,1,1],[0,0,0]],
            [[0,1,1],[0,1,0],[0,1,0]],
            [[0,0,0],[1,1,1],[0,0,1]],
            [[0,1,0],[0,1,0],[1,1,0]]
        ],
    "O":[
            [[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]],
            [[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]],
            [[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]],
            [[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]]
        ]
}

class Piece:
    def __init__(self, mino):
        self.mino, self.mino_index = mino, mino_types.index(mino)
        self.rotation_state = 0
        self.shape = []
        self.shape_update()

    # Update shape value based on current rotation state.
    def shape_update(self):
        self.shape = mino_shapes[self.mino][self.rotation_state]
    
    # return shape value with 0, 1
    def get_shape(self):
        return self.shape
    
    # return shape value with mino index
    def get_colored_shape(self):
        return list(map(lambda x : (list(map(lambda i : i * self.mino_index, x))), self.shape))
    
    # Rotate minos by num * 90 degree Clockwise. num need to be an integer value.
    def rotate(self, num:int):
        self.rotation_state = (self.rotation_state + num) % 4
        self.shape_update()
    
