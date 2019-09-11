from IPython.display import clear_output
def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])




def player_input():
    '''
    output =(player1 marker ,player 2 marker)
    '''
    marker=''
    
    
    while marker != 'X' and marker != 'O':
        marker= input('player 1 choose X or O').upper()
    
    if marker == 'X':
        return ('X','O')
    else:
        return('O','X')
        


def place_marker(board,marker,position):
    if space_check(board,position):
        board[position]=marker
    else:
        print('please choose other position')
        place_marker(board,marker,player_choice(board))

def win_check(board,mark):
        return((board[7]==mark and board[8]==mark and board[9]==mark) or
           (board[4]==mark and board[5]==mark and board[6]==mark) or
           (board[1]==mark and board[2]==mark and board[3]==mark) or
           (board[7]==mark and board[4]==mark and board[1]==mark) or
           (board[8]==mark and board[5]==mark and board[2]==mark) or
           (board[3]==mark and board[6]==mark and board[9]==mark) or
           (board[7]==mark and board[5]==mark and board[3]==mark) or
           (board[9]==mark and board[5]==mark and board[1]==mark))    


import random
def choose_first():
    
    flip=random.randint(0,1)
    
    if flip==0:
        return 'palyer1'
    else:
        return 'player2'


def space_check(board,position):
    if board[position]==' ':
        return(True)

def full_board(board):
    for i in range(1,10):
        if space_check(board,i):
            return(False)
    return(True)

def player_choice(board):
    position= 0
    while position not in range(1,10) and space_check(board,position):
        position=int(input('please chose a position (1-9)'))
    return position

def replay():
    choice =input('do you want to play again answer yes or no').upper()
    return choice == 'YES'



print ('welcome to tic tac toe')


while True:
    the_board=[' ']*10
    player1,player2 =player_input()
    turn=choose_first()
    print(turn + ' will go first')
    
    play_game= input('ready to play game? y or n ').lower()
    
    if play_game=='y':
        game_on = True
    else:
        game_on=False
    print (turn)
    while game_on:
        if turn == 'player1':
            display_board(the_board)
            print('player 1 turn')
            position= player_choice(the_board)
            place_marker(the_board,player1,position)
            if win_check(the_board,player1):
                display_board(the_board)
                print('player 1 has won' )
                game_on= False
            else:
                if full_board(the_board):
                    display_board(the_board)
                    print('the game is tie')
                    game_on= False
                else:
                    turn='player2'
        else:
            display_board(the_board)
            print('player 2 turn')
            position= player_choice(the_board)
            place_marker(the_board,player2,position)
            if win_check(the_board,player2):
                display_board(the_board)
                print('player 2 has won' )
                game_on= False
            else:
                if full_board(the_board):
                    display_board(the_board)
                    print('the game is tie')
                    game_on= False
                else:
                    turn= 'player1'            
    
    if not replay():
        break
    







        