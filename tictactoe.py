"""
Tic Tac Toe Player
"""

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

    x_count = 0
    o_count = 0
    # the game started now
    for row in board:
        x_count += row.count(X)
        o_count += row.count(O)

    if x_count > o_count:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            # see if it is not empty
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))

    return possible_actions


def result(board, action):
    import copy
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if board[i][j] != EMPTY:
        raise Exception
    current_player = player(board)
    new_board = copy.deepcopy(board)
    new_board[i][j] = current_player
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # if X wins
    for i in range(3):
        if all(board[i][j] == X for j in range(3)):
            return X
    for j in range(3):
        if all(board[i][j] == X for i in range(3)):
            return X
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    if board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return X

    # if O wins

    for i in range(3):
        if all(board[i][j] == O for j in range(3)):
            return O
    for j in range(3):
        if all(board[i][j] == O for i in range(3)):
            return O
    if board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return X
    if board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    if any(row.count(EMPTY) > 0 for row in board):
        return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    the_winner = winner(board)
    if the_winner == X:
        return 1
    elif the_winner == O:
        return -1
    else:
        return 0


def max_value(board):
    if terminal(board):
        return utility(board), None
    v = -2
    for action in actions(board):
        temporary, _ = min_value(result(board, action))
        # if temporary == 1:
        #     return temporary, action
        if temporary >= v:
            v = temporary
            final_action = action
    return v, final_action


def min_value(board):
    if terminal(board):
        return utility(board), None
    v = 2
    for action in actions(board):
        temporary, _ = max_value(result(board, action))
        # if temporary == -1:
        #     return temporary, action
        if temporary <= v:
            v = temporary
            final_action = action
    return v, final_action


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        _, final_action = max_value(board)
    else:
        _, final_action = min_value(board)
    return final_action


board = initial_state()
board[0][1] = O
board[0][2] = X
board[1][1] = X
board[1][2] = O

print(minimax(board))
