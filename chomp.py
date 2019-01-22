import numpy as np
import pandas as pd
import random

EMOJI = {-1: '\u2612', 0: ' ', 1: '\u2610'}


class ChompGame:
    def __init__(self, size == (3, 4)):
        self.p1 = Player()
        self.p2 = Player()
        self.turn = random.choice([self.p1, self.p2])

    def board_length( self, size):
        self.size = size
        self.size = [(3, 4), (6, 7), (10, 10)]
        yelp = input('Choose your board size. You get to choose between sizes: 3 x 4, 6 x 7, 10 x 10. You choose:')
        size1 = "(3,4)" or "3 x 4" or "3x4"
        size2 = "(6,7)" or "6 x 7" or "6x7"
        size3 = "(10,10)" or "10 x 10" or "10x10"
        if int(yelp) == size1:
            return size == (3, 4)
        if int(yelp) == size2:
            return size == (6, 7)
        if int(yelp) == size3:
            return size == (10, 10)

    def __repr__(self):
        return f'ChompGame(size = {self.size},

class Board:
    def __init__(self, rows, cols):
        # Use a 2d array to store board state
        # ones for chocolate, zeros for eaten squares, and -1 for poison
        self.rows = rows
        self.cols = cols
        self.state = np.ones((rows, cols), dtype=int)
        self.state[-1][0] = -1

    def __repr__(self):
        return f'Board({self.rows}, {self.cols})'

    def __str__(self):
        col_idx = range(self.cols)
        row_idx = [chr(letter) for letter in range(65, 65+self.rows)]
        board_emoji = np.array([[EMOJI[val] for val in row] for row in self.state])
        board_df = pd.DataFrame(data=board_emoji, index=row_idx, columns=col_idx)
        return str(board_df)

    def take(self, row, col):
        for r in range(row + 1):
            self.state[r][col:] = 0

class Player:
    def __init__(self, score = 0, name = None):
        self.score = score
        self.name = name
        self.name = input('Enter your name:')

    def __repr__(self):
        return f'Player(score = {self.score}, name = {self.name})'
