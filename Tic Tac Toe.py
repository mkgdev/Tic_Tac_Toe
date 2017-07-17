from __future__ import print_function
import random



def display_board(board):
    print(board[6], '|', board[7], '|', board[8])
    print('----------')
    print(board[3], '|', board[4], '|', board[5])
    print('----------')
    print(board[0], '|', board[1], '|', board[2])


def player_input():
    print('Player 1 : Do you want "X" or "O"?')
    player1 = raw_input()
    while player1 != 'X' and player1 != 'O':
        print('Please choose only "X" or "O"')
        player1 = raw_input()
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    print('Player1 chose', player1)
    print('Player2 chose', player2)


    return [player1, player2]  # returning the list of marker of players


def place_marker(board, marker, position):
    board[position] = marker
    display_board(board)


def choose_first():  # Assign first turn
    draw = random.randint(0, 1)  # generate random number either '0' or '1'
    if draw == 0:
        return ['player1', 'player2']
    else:
        return ['player2', 'player1']


def space_check(board, position):  # Check if chosen position is empty or not
    if board[position] == " ":
        return True
    else:
        return False


def full_board_check(board):  # Check if board is still empty or not
    for item in board:
	print(item)
        if item == ' ':
            return True

    return False


def win_check(board, mark):
    index = 0
    while index <= 8:

        # if %3==0
        if index % 3 == 0:

            # check the same marker horizontally
            i = index
            while i <= index + 2:
                if board[i] != mark:
                    break

                i += 1
            if i > index + 2:
                return True

                # if >=0 and <=2
        if index >= 0 and index <= 2:

            # check vertically
            i = index
            while i <= index + 6:
                if board[i] != mark:
                    break
                i += 3

            if i > index + 6:
                return True


                # check diagonally for only %2==0
            if index % 2 == 0:
                i = index

                # if position is 0
                if index == 0:
                    increment = 4
                # if position is 2
                if index == 2:
                    increment = 2

                while i <= index + increment * 2:
                    if board[i] != mark:
                        break
                    i = i + increment

                if i > index + increment * 2:
                    return True

        index = index + 1

    return False


def replay():
    print('Enter y to continue, n to exit')
    ans = raw_input()
    if ans == 'y':
        return True
    else:
        return False


print('Welcome to Tic Tac Toe Game!')


while replay():

    board = [" "] * 9
    markerList = player_input()  # Player 1 choice return to marker
    display_board(board)
    player1 = markerList[0]  # saving the player1 marker
    player2 = markerList[1]  # saving the player2 marker

    turn = choose_first()
    if (turn[0] == 'player2'):  # swap function
        temp = player2
        player2 = player1
        player1 = temp


    while True:
        print('Enter your position 1-9', turn[0])
        pos = int(input())

        # check for available spaces
        while space_check(board, pos-1) == False:

            print('position already filled! Enter position again')
            pos = int(input())
        else:

            place_marker(board, player1, pos-1)

        # check for win
        if win_check(board, player1):
            print(turn[0], 'win')
            break

	 # check if still space available
        if full_board_check(board)==False:
            # if available
            print('Match draw')
            break

        print('Enter your position 1-9', turn[1])
        pos = int(input())

        # check for avaiable spaces

        while space_check(board, pos-1) == False:

            print('position already filled! Enter position again')
            pos = int(input())

        else:
            place_marker(board, player2, pos-1)
        # check for win
        if win_check(board, player2):
            print(turn[1], 'win')
            break

       

    print('Wanna  replay? Enter y/n')
    
  



