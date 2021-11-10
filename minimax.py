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
        value = -float("inf")
        moves = self.generateMoves(board, self.side)
        bestMove = []
        alpha = -float("inf")
        beta = float("inf")
        if len(moves) == 0:
            return []
        for move in moves:
            temp = self.minimax(self.nextBoard(board, self.side, move),
                self.limit - 1, False, alpha, beta)
            if (temp > value):
                value = temp
                bestMove = move
            alpha = max(alpha, value)
        return bestMove
    def minimax(self, board, depth, isMax, alpha, beta):
        if depth == 0:
            return self.eval(board)
        elif isMax:
            return self.maximize(board, depth, alpha, beta)
        else:
            return self.minimize(board, depth, alpha, beta)
    def maximize(self, board, depth, alpha, beta):
        value = -float("inf")
        moves = self.generateMoves(board, self.side)
        if (len(moves) == 0):
            return value
        for move in moves:
            temp = self.minimax(self.nextBoard(board, self.side, move),
                        depth - 1, False, alpha, beta)
            value = max(temp, value)
            if (value >= beta):
                break
            alpha = max(alpha, value)
        return value
    def minimize(self, board, depth, alpha, beta):
        value = float("inf")
        moves = self.generateMoves(board, self.opponent(self.side))
        if (len(moves) == 0):
            return value
        for move in moves:
            temp = self.minimax(self.nextBoard(board, self.opponent(self.side), move),
                        depth - 1, True, alpha, beta)
            value = min(temp, value)
            if (value <= alpha):
                break
            beta = min(beta, value)
        return value
    def eval(self, board):
        moves = self.generateMoves(board, self.side)
        value = len(moves)
        for r in range(len(board)):
            if (board[r][0] == self.side):
                value += 2
        for r in range(len(board)):
            if (board[r][len(board) - 1] == self.side):
                value += 2
        for c in range(len(board)):
            if (board[0][c] == self.side):
                value += 2
        for c in range(len(board)):
            if (board[len(board) - 1][c] == self.side):
                value += 2
        for r in range(len(board)):
            for c in range(len(board)):
                if (r != 0 and r != len(board) - 1):
                    if (board[r - 1][c] == board[r + 1][c]):
                        value += 1
                if (c != 0 and c != len(board) - 1):
                    if (board[r][c - 1] == board[r][c + 1]):
                        value += 1
        for move in moves:
            value += 2 * self.distance(move[0], move[1], move[2], move[3])
        return value

# Need these lines in this file in order to test the MinimaxPlayer class
# Comment out these lines in the konane.py file so it's not run twice
game = Konane(8)
game.playNGames(1, MinimaxPlayer(8, 2), HumanPlayer(), 1)
