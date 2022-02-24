import math
import random
from re import L


class Player:
    def __init__(self, letter):
        # letter is X or O
        self.letter = letter

    # we want all players to get their next move given a game
    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')
            # check for a correct value of input by casting it to an integer
            # if it's not an integer, we will say the move is invalid
            # if the spot is not available on the board, we will say invalid move
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True  # if these are successful, great!
            except ValueError:
                print('Invalid square. Try again.')
        return val
