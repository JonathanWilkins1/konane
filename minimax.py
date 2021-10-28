### File: minimax.py
### Classes defined: MinimaxPlayer

from konane import *

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
            return []
        value = self.minimax(board, self.limit, True)
        print(value)
        for move in moves:
            if value == self.eval(self.nextBoard(board, self.side, move)):
                return move
        return []
    def minimax(self, board, depth, isMax):
        if depth == 0:
            return self.eval(board)
        elif isMax:
            return self.maximize(board, depth)
        else:
            return self.minimize(board, depth)
    def maximize(self, board, depth):
        value = -float("inf")
        moves = self.generateMoves(board, self.side)
        if (len(moves) == 0):
            return float("inf")
        for move in moves:
            value = max(self.minimax(self.nextBoard(board, self.opponent(self.side), move),
                        depth - 1, False), value)
        return value
    def minimize(self, board, depth):
        value = float("inf")
        moves = self.generateMoves(board, self.opponent(self.side))
        if (len(moves) == 0):
            return -float("inf")
        for move in moves:
            value = min(self.minimax(self.nextBoard(board, self.side, move),
                        depth - 1, True), value)
        return value
    def eval(self, board):
        return len(self.generateMoves(board, self.side))

    ############# looking too far, take a step back and stop recursing before stepping down
    #############   into a terminal state and getting inf or -inf for len(generateMoves)


# Need these lines in this file in order to test the MinimaxPlayer class
# Comment out these lines in the konane.py file so it's not run twice
game = Konane(8)
game.playNGames(1, MinimaxPlayer(8, 2), SimplePlayer(8), 1)
