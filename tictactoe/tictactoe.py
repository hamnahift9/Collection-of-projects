"""
Tic Tac Toe Player
Done as part of Cs50ai
"""

import math
import copy

from sqlalchemy import true

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

    #Keep track of number of moves
    moves = 0;

    #Count number of moves
    for row in board:
        for cell in row:
            if cell != EMPTY:
                moves += 1 
    
    #Return player according to the number of moves
    if moves == 9:
        return EMPTY
    elif moves % 2 == 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    i = 0
    j = 0
    for row in board:
        for cell in row:
            if cell == EMPTY:
                actions.add((i,j))
        j += 1
    i += 1
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    move = player(board)

    copy_board = copy.deepcopy(board)

    #Return exception if cell isn't empty
    if copy_board[action[0]][action[1]] != EMPTY:
        raise Exception
    copy_board[action[0]][action[1]] == move

    return copy_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for player in [X,O]:
        #Keep track of current cell and count
        
        j = 0
        i = 0
        count = 0

        #Checks for vertical wins 
        #Iterate through rows
        while i in range(0,3):
            #If current cell is equal to player: increment count and i by 1 
            if board[i][j] == player:
                count +=1 
                i+=1

            #Else reset row and count to 0 and increment j by 1 
            else:
                j+=1
                i = 0
                count= 0
                #Break loop if j is 3 
                if j == 3:
                    break
            
            #If count is 3 declare current player the winner
            if count == 3: 
                return player 
    
        #Check for horizontal wins
        i= 0
        j=0
        count=0
        #Iterate through rows 
        while i in range(0,3):
            if board[i][j] == player:
                count+= 1 
                j+=1 
            else:
                i+=1 
                j=0
                count=0
            if count == 3: 
                return player
        
        #Check first diagonal
        i=0
        j=0
        count=0
        while i in range(0,3):
            if board[i][j] == player:
                i+=1
                j+=1 
                count+=1
            else:
                break 
            if count == 3:
                return player
        
        #Check second diagonal
        i=0
        j=2
        count=0
        while i in range(0,3):
            if board[i][j] == player:
                i+=1
                j-=1
                count+=1 
            else:
                break
            if count == 3:
                print(player)
                return player
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    elif player(board) == EMPTY:
        return True

    return False



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1

    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    def max_value(board):
        acts = ()
        if terminal(board):
            return utility(board), acts
        else:
            v = int("-inf")
            for action in actions(board):
                minv = min_value(result(board, action))[0]
                if minv > v:
                    v = minv
                    acts = action
            return v, acts

    def min_value(board):
        acts = ()
        if terminal(board):
            return utility(board), acts
        else:
            v = int("inf")
            for action in actions(board):
                maxv = max_value(result(board, action))[0]
                if maxv < v:
                    v = maxv
                    acts = action
            return v, acts

    player = player(board)

    if terminal(board):
        return None

    if player == X:
        return max_value(board)[1]

    else:
        return min_value(board)[1]
