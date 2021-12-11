# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 15:05:26 2021

@author: ADITI
"""

import sys 

#Constants used for dispalying the board
empty_space ="."
player_x = "X"
player_O = "O"

Board_width = 7
Board_height = 6
Column_labels = ('1','2','3','4','5','6','7')
assert len(Column_labels) == Board_width

def main():
    print("****************Four In a Row********************")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    
    print("How To play the game :-")
    print("-> Two players take turns dropping tiles into one of seven columns,")
    print("trying to make four in a row horizontally, vertically or diagonaally.")
    
    
    #Set up a new game
    gameboard = GetNewBoard()
    playerTurn = player_x
    
    while True: # Running a player's turn
        #Display the board and get the player's move
        displayBoard(gameboard)
        playerMove = askForPlayerMove(playerTurn,gameboard)
        
        gameboard[playerMove] = playerTurn
        
        #Check for win or tie
        if isWinner(playerTurn,gameboard):
            displayBoard(gameboard)
            print("PLAYER  " + playerTurn + " has WON !!!!!")
            sys.exit()
            
        elif isFull(gameboard):
            displayBoard(gameboard)
            print("It is a TIE.")
            sys.exit()
            
        #Switch turns to other players
        if playerTurn == player_x:
            playerTurn = player_O
        elif playerTurn == player_O:
            playerTurn = player_x
            
        # Returning a dictionary representing Four in a row
        # the keys of the dictionary are "columnIndex" and "rowIndex"
        # Values of the dictionary are "X" , "O" or ".(empty space)"

def GetNewBoard():
        board = {}
        for columnIndex in range(Board_width):
            for rowIndex in range(Board_height):
                board[(columnIndex,rowIndex)] = empty_space
        return board
    
def displayBoard(board):
        # prepare a list to pass the format() string method for the board template.
        # list holds the board's tiles going left to right, top to bottom
        
        tileChars = []
        for rowIndex in range(Board_height):
            for columnIndex in range(Board_width):
                tileChars.append(board[(columnIndex,rowIndex)])
                
        # displaying the board:
        print("""
                  1234567
             +---------------+
                 |{}{}{}{}{}{}{}|
                 |{}{}{}{}{}{}{}|
                 |{}{}{}{}{}{}{}|
                 |{}{}{}{}{}{}{}|
                 |{}{}{}{}{}{}{}|
                 |{}{}{}{}{}{}{}|
             +---------------+""".format(*tileChars))
             
def askForPlayerMove(playerTile,board):
        # Let the player select a column on the board to drop a tile into.
        
        while True:
            print("Player {}, Enter a column or press -1 to Quit".format(playerTile))
            response = input('>').upper().strip()
            
            if response == '-1':
                print("Thankyou for playing.")
                sys.exit()
                
            if response not in Column_labels:
                print('Please enter a number from 1 to {}'.format(Board_width))
                continue # asking for valid move from player
                
            columnIndex = int(response) -1 #-1 for the 0 based index
            
            #if the column is full, ask for a move again:
            if board[(columnIndex,0)] != empty_space:
                print('That column is full, select another one.')
                continue # asking for valid move from player
                
            #Starting from the bottom and finding the first empty space
            for rowIndex in range(Board_height-1,-1,-1):
                if board[(columnIndex,rowIndex)] == empty_space:
                    return (columnIndex,rowIndex)
                
def isFull(board):
        #returns true if the board has no empty spaces else false.
        for rowIndex in range(Board_height):
            for columnIndex in range(Board_width):
                 if board[(columnIndex,rowIndex)] == empty_space:
                     return False
        return True

def isWinner(playerTile,board):
        #returns True if the playertile has Four tiles in a row else False
        
        for columnIndex in range(Board_width-3):
            for rowIndex in range(Board_height):
                #Checking for four in a row moving horizontally!
                tile1 = board[(columnIndex,rowIndex)]
                tile2 = board[(columnIndex+1,rowIndex)]
                tile3 = board[(columnIndex+2,rowIndex)]
                tile4 = board[(columnIndex+3,rowIndex)]
                if tile1 == tile2 == tile3 == tile4 == playerTile:
                    return True
                
        for columnIndex in range(Board_width):
            for rowIndex in range(Board_height-3):
                #Checking for four in a row moving Verically!
                tile1 = board[(columnIndex,rowIndex)]
                tile2 = board[(columnIndex,rowIndex+1)]
                tile3 = board[(columnIndex,rowIndex+2)]
                tile4 = board[(columnIndex,rowIndex+3)]
                if tile1 == tile2 == tile3 == tile4 == playerTile:
                    return True
                
        for columnIndex in range(Board_width-3):
            for rowIndex in range(Board_height-3):
                #Checking for four in a row moving diagonally in right-down!
                tile1 = board[(columnIndex,rowIndex)]
                tile2 = board[(columnIndex+1,rowIndex+1)]
                tile3 = board[(columnIndex+2,rowIndex+2)]
                tile4 = board[(columnIndex+3,rowIndex+3)]
                if tile1 == tile2 == tile3 == tile4 == playerTile:
                    return True
                
                 #Checking for four in a row moving diagonally in left-down!
                tile1 = board[(columnIndex+3,rowIndex)]
                tile2 = board[(columnIndex+2,rowIndex+1)]
                tile3 = board[(columnIndex+1,rowIndex+2)]
                tile4 = board[(columnIndex,rowIndex+3)]
                if tile1 == tile2 == tile3 == tile4 == playerTile:
                    return True
        return False
    
if __name__ == "__main__":
    main()

