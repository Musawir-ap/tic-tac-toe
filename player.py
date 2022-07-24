import random


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
