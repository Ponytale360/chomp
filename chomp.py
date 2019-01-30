import numpy as np
import pandas as pd
import random
import itertools

EMOJI = {-1: '\u2612', 0: ' ', 1: '\u2610'}


class ChompGame:
    """Contains the control flow for the game"""
    def __init__(self, n_players=2, size=(3, 4), m_player=1, p_player=1):
        self.n_players = n_players
        self.size = size
        self.board = Board(*size)
        self.m_player = m_player
        self.p_player = p_player
        self.game_over = False
        self.players = [m_player, p_player]
        self.order_of_players = []
        self.current_player = None

    def __repr__(self):
        return f'ChompGame({self.n_players}, {self.size})'

    def play(self):
        self.setup()
        while not self.game_over:
            for k in self.order_of_players:
                print(f'{k}, it\'s your turn!\n')
            print(self.board)
            self.move()
            yield itertools.cycle(self.order_of_players)
            if self.board.state[-1][0] == 0:
                self.game_over = True
                self.current_player.wins -= 1

    def setup(self):
        for i in range(1, self.n_players + 1):
            print(f'***Player {i}***')
            self.players.append(Player())

        self.current_player = random.choice(self.players)

        if self.current_player == self.p_player:
            self.order_of_players = [self.current_player, self.m_player]
        if self.current_player == self.m_player:
            self.order_of_players = [self.current_player, self.p_player]

    def move(self):
        coord_str = input("Enter the coordinates for your move. (e.g. A3)")
        row_str, col_str = coord_str[0].upper(), coord_str[1]
        row = ord(row_str) - 65
        col = int(col_str)
        self.board.take(row, col)


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
        # self.state[:row+1, col:] = 0
        for r in range(row + 1):
            self.state[r][col:] = 0


class Player:
    def __init__(self):
        self.name = input("\tEnter your name: ")
        self.wins = 0

    def __repr__(self):
        return f'Player({self.name})'

    def __str__(self):
        return self.name


if __name__ == "__main__":
    ChompGame().play()
