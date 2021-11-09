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
            lisp = self.minimax(self.nextBoard(board, self.side, move),
                self.limit - 1, False, -float("inf"), float("inf"))
            if (lisp[0] > value):
                value = lisp[0]
                bestMove = move
        return bestMove
    def minimax(self, board, depth, isMax, alpha, beta):
        if depth == 0:
            return [self.eval(board), alpha, beta]
            # return lisp[0] if (depth == self.limit - 1) else lisp
        elif isMax:
            return self.maximize(board, depth, alpha, beta)
            # return lisp[0] if (depth == self.limit - 1) else lisp
        else:
            return self.minimize(board, depth, alpha, beta)
            # return lisp[0] if (depth == self.limit - 1) else lisp
    def maximize(self, board, depth, alpha, beta):
        value = -float("inf")
        moves = self.generateMoves(board, self.side)
        if (len(moves) == 0):
            return [value, alpha, value]
        for move in moves:
            lisp = self.minimax(self.nextBoard(board, self.side, move),
                        depth - 1, False, alpha, beta)
            value = max(lisp[0], value)
            if (value >= beta):
                break
        return [value, alpha, value]
    def minimize(self, board, depth, alpha, beta):
        value = float("inf")
        moves = self.generateMoves(board, self.opponent(self.side))
        if (len(moves) == 0):
            return [value, value, beta]
        for move in moves:
            lisp = self.minimax(self.nextBoard(board, self.opponent(self.side), move),
                        depth - 1, True, alpha, beta)
            value = min(lisp[0], value)
            if (value <= alpha):
                break
        return [value, value, beta]
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
