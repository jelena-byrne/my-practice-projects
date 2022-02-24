from tkinter import dialog
from player import HumanPlayer, RandomComputerPlayer
import time


class TicTacToe:
    def __init__(self) -> None:
        # we will ue a single list to represent 3x3 board
        self.board = [' ' for _ in range(9)]
        self.current_winner = None  # keep track of winner!

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row)+' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)]
                        for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row)+' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # moves = []
        # for (i,x) in enumerate(self.board):
        #     # ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
        #     if spot == ' ':
        #         moves.append(i)
        # return moves

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')
        # OR return len(self.available_moves())

    def make_move(self, square, letter):
        # if it's a valid move, then perform it (assign square to a letter) then return True
        # if the move is invalid, return False
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        else:
            return False

    def winner(self, square, letter):
        # winner if 3 in a row anywhere, we have to check all
        # first, check the row:
        row_ind = square // 3
        row = self.board[row_ind*3: (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # check column:
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check diagonals (only even numbers, [0,2,4,6,8] since they're the only possible moves for diagonal to win):
        if square % 2 == 0:
            diagonal1 = [self.board[i]
                         for i in [0, 4, 8]]  # left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i]
                         for i in [2, 4, 6]]  # right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True

        # if all the checks fail:
        return False


def play(game, x_player, o_player, print_game=True):
    # returns the winner of the game (letter of winner)! or None if a tie
    if print_game:
        game.print_board_nums()

    letter = 'X'  # starting letter
    # iterate while the game still has empty squares
    while game.empty_squares():
        # get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # define a function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')  # just an empty line

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')

            # after we made the move, we need to alternate the letters
            letter = 'O' if letter == 'X' else 'X'  # switches player
            # if letter == 'X':
            #     letter = 'O'
            # else:
            #     letter = 'X'

        # add in a pause between human and computer moves to make it more realistic
        time.sleep(1.5)

    if print_game:
        print('It\'s a tie!')


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
