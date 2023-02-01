"""
Tic Tac Toe Player
"""

import math
import copy

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
    moves = 0
    for row in board:
        for col in row:
            if col == X or col == O:
                moves += 1

    if moves == 0:
        return X
    elif moves % 2 == 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == EMPTY:
                actions.add((i, j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    state_board = copy.deepcopy(board)
    possible_actions = actions(state_board)
    if not action in possible_actions:
        raise Exception()

    actual_player = player(state_board)
    i, j = action
    state_board[i][j] = actual_player
    return state_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Horizontal wins
    for row in board:
        if all(col == X for col in row):
            return X
        elif all(col == O for col in row):
            return O

    # Vertical wins
    for col in range(3):
        countX = 0
        countO = 0
        for row in range(3):
            if board[row][col] == X:
                countX += 1
            elif board[row][col] == O:
                countO += 1
        if countX == 3:
            return X
        if countO == 3:
            return O

    # Left diagonal wins
    countX = 0
    countO = 0
    for index in range(3):
        if board[index][index] == X:
            countX += 1
        elif board[index][index] == O:
            countO += 1
        if countX == 3:
            return X
        if countO == 3:
            return O

    # Right diagonal wins
    countX = 0
    countO = 0
    col = 2
    for row in range(3):
        if board[row][col] == X:
            countX +=1
        elif board[row][col] == O:
            countO += 1
        if countX == 3:
            return X
        if countO == 3:
            return O
        col -= 1

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # If there is a winner, game is over
    if winner(board):
        return True

    # If there is empty space, game is not over
    for row in board:
        if any(col != X and col != O for col in row):
            return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board=board)
    if not winner_player:
        return 0

    if winner_player == X:
        return 1
    else:
        return -1


score = 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    optimal_action = None
    alpha = -math.inf
    beta = math.inf
    if player(board) == X:  # Maximizing player
        evaluation = -math.inf
        for action in actions(board):
            score = minValue(result(board, action), alpha, beta)
            if score > evaluation:
                evaluation = score
                optimal_action = action
        return optimal_action

    # Minimizing player
    else:
        evaluation = math.inf
        for action in actions(board):
            score = maxValue(result(board, action), alpha, beta)
            if score < evaluation:
                evaluation = score

                optimal_action = action
        return optimal_action



def maxValue(board, alpha, beta):
    if terminal(board):
        return utility(board)
    evaluation = -math.inf
    for action in actions(board):
        evaluation = max(evaluation, minValue(result(board, action), alpha, beta))
        alpha = max(alpha, evaluation)
        if beta <= alpha:
            break;
    return evaluation

def minValue(board, alpha, beta):
    if terminal(board):
        return utility(board)
    evaluation = math.inf
    for action in actions(board):
        evaluation = min(evaluation, maxValue(result(board, action), alpha, beta))
        beta = min(beta, evaluation)
        if beta <= alpha:
            break;
    return evaluation