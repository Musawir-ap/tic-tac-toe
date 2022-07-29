import time

from player import HumanPlayer, RandomComputerPlayer, GeniusComputer


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_num():
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_spots(self):
        return ' ' in self.board

    def num_empty_spots(self):
        return self.board.count(' ')

    def make_move(self, spot, letter):
        if self.board[spot] == ' ':
            self.board[spot] = letter
            if self.winner(spot, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, spot, letter):
        # checking for row
        row_index = spot // 3
        row = self.board[row_index * 3: (row_index + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # checking for column
        col_index = spot % 3
        col = [self.board[col_index + i * 3] for i in range(3)]
        if all([spot == letter for spot in col]):
            return True

        # checking for diagonal
        if spot % 2 == 0:  # (0,2,4,6,8)
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False


def play(game, x_player, o_player, print_board=True):
    if print_board:
        game.print_board_num()

    letter = 'X'
    while game.empty_spots():
        if letter == 'O':
            spot = o_player.get_moves(game)
        else:
            spot = x_player.get_moves(game)

        if game.make_move(spot, letter):
            if print_board:
                print(f'{letter} made a move to spot {spot}')
                game.print_board()
                print('')
            if game.current_winner:
                if print_board:
                    print(letter + ' wins!')
                return letter

            letter = 'O' if letter == 'X' else 'X'
        time.sleep(0.8)

    if print_board:
        print('It is a tie!')


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = GeniusComputer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_board=True)
