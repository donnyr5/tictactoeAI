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

    xx = 0
    oo = 0

    #iterate through the board and count the X and O
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                xx = xx + 1
            if board[i][j] == O:
                oo = oo + 1

    #compare
    if (xx > oo):
        return O
    else:
        return X
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    list = []
    #iterate through the board and return all EMPTY pairs
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                list.append((i,j))

    return list


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #check if valid action input
    if len(action) != 2:
        raise Exception
    if (action[0] < 0 or action[0] > 2):
        raise Exception
    if (action[1] < 0 or action[1] > 2):
        raise Exception
    
    i = action[0]
    j = action[1]

    if (board[i][j] != EMPTY):
        raise Exception
    
    # deep copy because for python it would otherwise change the old board.
    newBoard = copy.deepcopy(board)
    newBoard[i][j] = player(board) 

    return newBoard

def checkWinner(board, X):
    '''
    Helper function for winner to check X or O
    '''
    if (board[0][0] == X):          
        if (board[0][1] == X): 
            if (board[0][2] == X):      
                return True
        if (board[1][0] == X):
            if (board[2][0] == X):
                return True
        if (board[1][1] == X):
            if (board[2][2] == X):
                return True
    
    if (board[2][2] == X):
        if (board[1][2] == X):
            if (board[0][2] == X):
                return True
        if (board[2][1] == X):
            if (board[2][0] == X):
                return True
    
    if (board[1][1] == X):
        if (board[0][1] == X):
            if (board[2][1] == X):
                return True
        if (board[1][2] == X):
            if (board[1][0] == X):
                return True
        if (board[0][2] == X):
            if (board[2][0] == X):
                return True
    return None

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    #if X wins, return it, else O, else no winner (yet)
    if (checkWinner(board,X)):
        return X
    elif (checkWinner(board,O)):
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #if there is a winner the game is over, 
    if (winner(board) != None):
        return True
    else:
        for i in range(3):
            for j in range(3):
                if (board[i][j] == EMPTY):  
                    return False
        
        #all cells are occupied = game over
        return True
    

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if (winner(board) == X):
        return 1
    elif (winner(board) == O):
        return -1
    else:
        return 0
    

def minimax(board):
    """
    Returns the optimal action for the current player on the board.

    for pruning, if MIN is going, and a 1 pops up, we can stop that branch becuase we know MAX would take the 1.
    vise versa for MAX seeing a -1: MIN will take it so no need to continue that path of the tree.

    how do we know the action???
    """
    if terminal(board):
        return None

    alpha = -math.inf
    beta = math.inf

    if player(board) == X:  # MAX is playing
        return max_value(board, alpha, beta)[1]
    else:  # MIN is playing
        return min_value(board, alpha, beta)[1]


def max_value(board, alpha, beta):
    if terminal(board):
        return [utility(board), ()]

    v = -math.inf
    m = ()

    for action in actions(board):
        h = min_value(result(board, action), alpha, beta)[0]

        if h == 1:
            return [1, action]  # Found a winning move, no need to look further

        if h > v:
            v = h
            m = action

        alpha = max(alpha, v)

        if beta <= alpha:
            break  # Prune remaining branches

    return [v, m]

def min_value(board, alpha, beta):
    if terminal(board):
        return [utility(board), ()]

    v = math.inf
    m = ()

    for action in actions(board):
        h = max_value(result(board, action), alpha, beta)[0]

        if h == -1:
            return [-1, action]  # Found a losing move, no need to look further

        if h < v:
            v = h
            m = action

        beta = min(beta, v)

        if beta <= alpha:
            break  # Prune remaining branches

    return [v, m]






testBoard1 = [[X, EMPTY, EMPTY],
            [O, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

testBoard2 = [[X, EMPTY, EMPTY],
            [EMPTY, O, EMPTY],
            [EMPTY, EMPTY, X]]

testBoard6 = [[X, O, X],
            [X, O, O],
            [O, X, EMPTY]]

# print(actions(testBoard1))
# print(actions(testBoard2))

# print(result(testBoard1, (0,0)))
# print(result(testBoard1, (0,1)))

testBoard3 = result(testBoard2, (0,1))
testBoard4 = result(testBoard3, (1,2))
testBoard5 = result(testBoard4, (2,1))
print(testBoard5)

print(winner(testBoard1))
print(winner(testBoard5))

print(terminal(testBoard2))
print(terminal(testBoard6))
print(terminal(testBoard5))

print(utility(testBoard6))
print(utility(testBoard5))

print(minimax(testBoard2) )


