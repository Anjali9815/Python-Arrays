# Tic Tac Toe Game

board = [' ' for x in range(9)]

def print_board():
    print('   |   |')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('   |   |')

def check_win(player):
    if (board[0] == player and board[1] == player and board[2] == player) or \
       (board[3] == player and board[4] == player and board[5] == player) or \
       (board[6] == player and board[7] == player and board[8] == player) or \
       (board[0] == player and board[3] == player and board[6] == player) or \
       (board[1] == player and board[4] == player and board[7] == player) or \
       (board[2] == player and board[5] == player and board[8] == player) or \
       (board[0] == player and board[4] == player and board[8] == player) or \
       (board[2] == player and board[4] == player and board[6] == player):
        return True
    else:
        return False

def check_tie():
    if ' ' not in board:
        return True
    else:
        return False

def play_game():
    print('Welcome to Tic Tac Toe!')
    print_board()
    while True:
        # Player X turn
        x_choice = int(input("Player X, enter your choice (1-9): "))
        if board[x_choice-1] == ' ':
            board[x_choice-1] = 'X'
            print_board()
            if check_win('X'):
                print('Player X wins!')
                break
            elif check_tie():
                print('Tie game!')
                break
        else:
            print('That space is already taken. Please try again.')
            continue
        
        # Player O turn
        o_choice = int(input("Player O, enter your choice (1-9): "))
        if board[o_choice-1] == ' ':
            board[o_choice-1] = 'O'
            print_board()
            if check_win('O'):
                print('Player O wins!')
                break
            elif check_tie():
                print('Tie game!')
                break
        else:
            print('That space is already taken. Please try again.')
            continue

play_game()