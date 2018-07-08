# Tic-Tac-Toe Game Problem using Adversarial Search - Minimax Problem

import random
import math

# Check whether any moves left or not
def checkForAvailableMoves(board):
    for i in range(3):
        for j in range(3):
            if(board[i][j] == '-'):
                return True

    return False



# Check whether Player is win or not
def evaluationFunction(board, player):
    # Check through rowwise for whether player arrange horizontally
    for r in range(3):
        if((board[r][0] == player) & (board[r][0] == board[r][1]) & (board[r][0] == board[r][2])):
            return True

    # Check through columnwise for whether player arrange vertically
    for c in range(3):
        if((board[0][c] == player) & (board[0][c] == board[1][c]) & (board[0][c] == board[2][c])):
            return True

    # Check whether player arrange two of board's diagonals
    if(((board[0][0] == player) & (board[0][0] == board[1][1]) & (board[0][0] == board[2][2])) | 
        ((board[0][2] == player) & (board[0][2] == board[1][1]) & (board[0][2] == board[2][0]))):
        return True

    return False



# Implementation of Minimax algorithm
def  miniMaxAlgorithm(board, turn):
    t = ' '
    if turn == 'X':
        t = 'O'
    else:
        t = 'X'
    if (evaluationFunction(board, t) == True):
        if t == 'X':
            return {'Score' : 10}
        elif t == 'O':
            return {'Score' : -10}

    if(checkForAvailableMoves(board) == False):
        return {'Score' : 0}

    
    movesArrRow = []
    movesArrcol = []
    movesArrScore = []
    
    for i in range(3):
        for j in range(3):
            if(board[i][j] == '-'):
                rowValue = i
                colValue = j
                scoreValue = 0
                
                board[i][j] = turn

                if(turn == 'X'):
                    result = miniMaxAlgorithm(board, 'O')
                    scoreValue = result['Score']
                    
                else:
                    result = miniMaxAlgorithm(board, 'X')
                    scoreValue = result['Score']
    

                board[i][j] = '-' 

                movesArrRow.append(rowValue)
                movesArrcol.append(colValue)
                movesArrScore.append(scoreValue)

    bestMoveRow = -1
    bestMoveCol = -1
    if (turn == 'X'):
        bestScore = -10000
        for i in range(len(movesArrScore)):
            if movesArrScore[i] > bestScore:
                bestScore = movesArrScore[i]
                bestMoveRow = movesArrRow[i]
                bestMoveCol = movesArrcol[i]
                
    elif (turn == 'O'):
        bestScore = 10000
        for i in range(len(movesArrScore)):
            if movesArrScore[i] < bestScore:
                bestScore = movesArrScore[i]
                bestMoveRow = movesArrRow[i]
                bestMoveCol = movesArrcol[i]
                
    return {'Score' : bestScore, 'row' : bestMoveRow, 'col' : bestMoveCol}
   


# Print Tic-Tac-Toe Board
def printBoard(board):
    # print ("**************************************************************************************************************")
    for i in range(3):
        for j in range(3):
            print (board[i][j], end = " ")
        print ()

    # print ("**************************************************************************************************************")
    print ()



# Check whether Player is win or not
def checkWinningFunction(board):
    # Check through rowwise for whether player arrange horizontally
    for r in range(3):
        if((board[r][0] == board[r][1]) & (board[r][0] == board[r][2])):
            return board[r][0]

    # Check through columnwise for whether player arrange vertically
    for c in range(3):
        if((board[0][c] == board[1][c]) & (board[0][c] == board[2][c])):
            return board[0][c]

    # Check whether player arrange two of board's diagonals
    if(((board[0][0] == board[1][1]) & (board[0][0] == board[2][2])) | 
        ((board[0][2] == board[1][1]) & (board[0][2] == board[2][0]))):
        return board[0][2]

    return '-'




# Tic-Tac-Toe Board
board = [['-' for x in range(3)] for y in range(3)]

#
choice = input("Do you want to start or let computer to play??(y/n) ")
if(choice != 'y'):
    # Randomly Choose value for Computer Player 'X'
    rowIndex = random.choice(range(0,3,1))
    columnIndex = random.choice(range(0,3,1))

    board[rowIndex][columnIndex] = 'X'
    printBoard(board)

while checkForAvailableMoves(board) != False:
    rowVal = (int)(input("Enter Row Value:  "))
    colVal = (int)(input("Enter Column Value: "))
    # t = miniMaxAlgorithm(board, 'O')
    board[rowVal][colVal] = 'O'
    printBoard(board)
    result = checkWinningFunction(board)
    if(result != '-'):
        print (result, " Win!!")
        break
    if(checkForAvailableMoves(board) == False):
        break

    
    t = miniMaxAlgorithm(board, 'X')
    board[t['row']][t['col']] = 'X'
    printBoard(board)
    result = checkWinningFunction(board)
    if(result != '-'):
        print (result, " Win!!")
        break

if(checkForAvailableMoves(board) == False):
    result = checkWinningFunction(board)
    if(result != '-'):
        print (result, " Win!!")
    elif(result == '-'):
        print ("Match Draw!")