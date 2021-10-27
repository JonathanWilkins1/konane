### File: minimax.py
### Classes defined: MinimaxPlayer

### using ... import * gave me an error in VS Code so I did the following instead
from konane import Konane, Player, RandomPlayer

class MinimaxPlayer(Konane, Player):
    """
    Uses Minimax alpha beta pruning to choose moves
    """
    def __init__(self, size, depthLimit):
        Konane.__init__(self, size)
        self.limit = depthLimit
    def initialize(self, side):
        self.side = side
        self.name = "InterestingName"
    def getMove(self, board):
        moves = self.generateMoves(board, self.side)
        if len(moves) == 0:
            return float("inf")
        elif self.openingMove(board):
            return moves[0]
        else:
            return eval(self, board, moves)
    def eval(self, board, moves):
        return moves[0]
        #complete this – this will be your evaluation function. High
        # values should be good for max.


### Need these lines in this file in order to test the MinimaxPlayer class
### Comment out these lines in the konane.py file so it's not run twice
game = Konane(4)
game.playNGames(1, MinimaxPlayer(4, 1), RandomPlayer(4), 1)