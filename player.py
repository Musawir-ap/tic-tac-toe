import random
import math

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_moves(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_moves(self, game):
        spot = random.choice(game.available_moves())
        return spot


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_moves(self, game):
        valid_spot = False
        val = None
        while not valid_spot:
            spot = input(self.letter + ' > enter your move (0-8) : ')
            try:
                val = int(spot)
                if val not in game.available_moves():
                    raise ValueError
                valid_spot = True
            except ValueError:
                print('Invalid spot, try again.')
        return val

class GeniusComputer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_moves(self, game):
        if len(game.available_moves()) == 9:
            spot = random.choice(game.available_moves())
        else:
            spot = self.minimax(game, self.letter)['position']
        return spot

    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        if  state.current_winner == other_player:
            return {'position': None,
                    'score': 1 * (state.num_empty_spots() + 1) if other_player ==max_player else
                    -1 * (state.num_empty_spots() + 1)
                    }
        elif not state.num_empty_spots():
            return {'position': None, 'score':0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)

            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best
