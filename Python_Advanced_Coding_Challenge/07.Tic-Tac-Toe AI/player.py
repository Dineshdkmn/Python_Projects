import random

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def get_move(self, game):
        while True:
            try:
                square = int(input(f"{self.letter}'s turn. Input move (0-8): "))
                if square not in game.available_moves():
                    raise ValueError("Invalid square. Please enter a number between 0 and 8.")
                return square
            except ValueError as e:
                print(e)

class RandomComputerPlayer(Player):
    def get_move(self, game):
        return random.choice(game.available_moves())

class SmartComputerPlayer(Player):
    def get_move(self, game):
        if len(game.available_moves()) == 9:
            return random.choice(game.available_moves())
        else:
            return self.minimax(game, self.letter)['position']

    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.board.count(' ') + 1) if other_player == max_player else -1 * (state.board.count(' ') + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': float('-inf')}
        else:
            best = {'position': None, 'score': float('inf')}
            
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