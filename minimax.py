### File: minimax.py
### Classes defined: MinimaxPlayer
### Authors: Jonathan Wilkins and Simon Schoelkopf

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
        value = -float("inf")
        bestMove = []
        for move in moves:
            temp = self.minimax(self.nextBoard(board, self.side, move),
                self.limit - 2, False)
            if (temp > value):
                value = temp
                bestMove = move
        return bestMove
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
            return self.eval(board)
        for move in moves:
            value = max(self.minimax(self.nextBoard(board, self.side, move),
                        depth - 1, False), value)
        return value
    def minimize(self, board, depth):
        value = float("inf")
        moves = self.generateMoves(board, self.opponent(self.side))
        if (len(moves) == 0):
            return self.eval(board)
        for move in moves:
            value = min(self.minimax(self.nextBoard(board, self.opponent(self.side), move),
                        depth - 1, True), value)
        return value
    def eval(self, board):
        value = len(self.generateMoves(board, self.side))
        for r in range(len(board)):
            if (board[r][0] == self.side):
                value += 1
        for r in range(len(board)):
            if (board[r][len(board) - 1] == self.side):
                value += 1
        for c in range(len(board)):
            if (board[0][c] == self.side):
                value += 1
        for c in range(len(board)):
            if (board[len(board) - 1][c] == self.side):
                value += 1
        return value

# Need these lines in this file in order to test the MinimaxPlayer class
# Comment out these lines in the konane.py file so it's not run twice
# game = Konane(8)
# game.playNGames(1, MinimaxPlayer(8, 2), SimplePlayer(8), 1)
