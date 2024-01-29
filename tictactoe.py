"""
Tic Tac Toe Player
"""

import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    if board == initial_state():
        return X

    x_num = 0
    o_num = 0

    # Count all the x's and o's 
    for row in board:
        x_num += row.count(X)
        o_num += row.count(O)

    # If x and o are at the same tally, X plays next.
    if x_num == o_num:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    actionsss = []

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actionsss.append([i, j])
    return actionsss
            

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newboard = copy.deepcopy(board)
    try:
        if newboard[action[0]][action[1]] != EMPTY:
            raise ValueError
        else:
            newboard[action[0]][action[1]] = player(newboard)
            return newboard
    except ValueError:
        print('Square already chosen')


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Check the rows for three of a kind. If so return winner
    for row in board:
        x_num = row.count(X)
        o_num = row.count(O)
        if x_num == 3:
            return X
        if o_num == 3:
            return O
    
    # Check columns for winner. If exists, return winner
    columns = []

    for j in range(len(board)):
        column = [row[j] for row in board]
        columns.append(column)

    for j in columns:
        x_num = j.count(X)
        o_num = j.count(O)
        if x_num == 3:
            return X
        if o_num == 3:
            return O

    # Check diagonals for winner. If so, return winner
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    if board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    if board[2][0] == X and board[1][1] == X and board[0][2] == X:
        return X
    if board[2][0] == O and board[1][1] == O and board[0][2] == O:
        return O

    # If there aren't three in a row, return tie
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
        
    if winner(board) is not None or not actions(board):
        return True
    else:
        return False 


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winning = winner(board)
    if winning == X:
        return 1
    elif winning == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    this_player = player(board)

    if this_player == X:
        v = -math.inf
        for action in actions(board):
            w = min_value(result(board, action))
            if w > v: 
                v = w
                move = action
    else:
        v = math.inf
        for action in actions(board):
            w = max_value(result(board, action))
            if w < v: 
                v = w
                move = action
    return move


def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions (board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions (board):
        v = min(v, max_value(result(board, action)))
    return v

