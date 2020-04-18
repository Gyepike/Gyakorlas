from IPython.display import clear_output

test_board = ['#',
              'o','O','X',
              'O','X','O',
              'o','O','X']
def player_input():
    print('Welcome tic Toe')
    player1 = input("kerem a markert 'X' vagy 'O' " ).lower()

    while (player1 != 'x'  and  player1 != 'o' ):
            print("Csak X vgy O lehet")
            player1 = input("kerem a markert 'X' vagy 'O' " ).lower()

    if player1 == "x":
         player2 = "o"
    else:
          player2 = "x"

    return "p1: " + player1 + " p2 :" + player2

def display_board(board):
    print('\n' * 100)
    print("-------")
    print('|'+board[7] + "|" + board[8] + "|" + board[9]+'|')
    print("-------")
    print('|'+board[4] + "|" + board[5] + "|" + board[6]+'|')
    print("-------")
    print('|'+board[1] + "|"+ board[2]  + "|" + board[3]+'|' )
    print("-------")


def place_marker(board, marker, position):
    board[position] = marker
    test_board = board


def win_check(board, mark):
    count = 0

    list1 = board[1] + board[4] + board[7]
    list2 = board[2] + board[5] + board[8]
    list3 = board[3] + board[6] + board[9]

    if (list3 == mark+mark+mark or list2 == mark+mark+mark or list1 == mark+mark+mark ):
         print("true")
         return  True;

    for i in board:
        if (i == mark.lower() or i == mark.upper()) :
            count +=1
            print(count)
            if (count == 3):
                return  True
        else:
            count =0

    return False

#kerem_markert()

print(win_check(test_board,"o"))
#test_board[1] = "D"
#display_board(test_board)

#place_marker(test_board,"*",8)
#display_board(test_board)
#print(player_input())
