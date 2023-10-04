import math
from copy import deepcopy
import numpy as np

X = 'X'
O = 'O'
EMPTY = None

def initial_state():
    
    return[[EMPTY,EMPTY,EMPTY],[EMPTY,EMPTY,EMPTY],[EMPTY,EMPTY,EMPTY]]

def get_diagonal(board):
    return[[board[0][0]],[board[1][1]],[board[2][2]],
           [board[0][2]],[board[1][1]],[board[2][0]]]
def get_columns(board):
    columns = []
    
    for i in range(3):
        columns.append(row[i] for row in board)
        
    return columns
def in_a_row(row):
    return all(val == row[0] for val in row) and row[0] is not None
 

def player(board):
    count_x=0
    count_o=0
    for i in board:
        for j in i:
            if(j=='X'):
                count_x=count_x+1
            if(j=='O'):
                count_o=count_o+1
    return O if count_x > count_o else X

def actions(board):
    
    action=set()
    for i, row in enumerate(board):
        for j, vall in enumerate(row):
            if(vall==EMPTY):
                action.add((i,j))
    return action

def result(board, action):
    i,j=action
    if(board[i][j]!=EMPTY):
        raise Exception("Invalid Move.")
    next_move=player(board)
    deep_board=deepcopy(board)
    deep_board[i][j]=next_move
    return deep_board


def winner(board):
    rows=board+get_diagonal(board)+get_columns(board)
    for row in rows:
        current_player=row[0]
        if current_player is not None and in_a_row(row):
            return current_player
    return None
def terminal(board):
    
    xx=winner(board)
    if(xx is not None):
        return True
    if(all(all(j!=EMPTY for j in i) for i in board)):
        return True
    return False

def utility(board):
    winner_player = winner(board)
    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    else:
        return 0

    
def max_alpha_beta_pruning(board, alpha, beta):
    if terminal(board):
        return utility(board), None
    vall = float("-inf")
    best = None
    for action in actions(board):
        min_val = min_alpha_beta_pruning(result(board, action), alpha, beta)[0]
        if min_val > vall:
            best = action
            vall = min_val
        alpha = max(alpha, vall)
        if beta <= alpha:
            break
    return vall, best

def min_alpha_beta_pruning(board, alpha, beta):
    if terminal(board):
        return utility(board), None
    vall = float("inf")
    best = None
    for action in actions(board):
        max_val = max_alpha_beta_pruning(result(board, action), alpha, beta)[0]
        if max_val < vall:
            best = action
            vall = max_val
        beta = min(beta, vall)
        if beta <= alpha:
            break
    return vall, best


def minmax(board):
    if terminal(board):
        return None
    if player(board) == X:
        return max_alpha_beta_pruning(board, float("-inf"), float("inf"))[1]
    elif player(board) == O:
        return min_alpha_beta_pruning(board, float("-inf"), float("inf"))[1]
    else:
        raise Exception("Error in Calculating Optimal Move")

        
    
            


