print("TIC TAC TOE")
b=["--","--","--",
    "--","--","--",
    "--","--","--",
   ]
current_player="X"
game_is_palying=True
winner=None

def display_board():

     print(b[0] + " | " + b[1] + " | " + b[2])
     print(b[3] + " | " + b[4] + " | " + b[5])
     print(b[6] + " | " + b[7] + " | " + b[8])

def handler():
    global current_player
    pos=int(input("enter position :"))
    print()
    b[pos]=current_player


def change_player():
    global current_player
    if current_player=="X":
        current_player="O"

    elif current_player=="O":
        current_player="X"

def check_winner():
    global winner
    winner1=check_row()
    winner2=check_col()
    winner3=check_dia()
    print("lets see who wins....")

    if winner1!=None:
        winner=winner1
        print("-----|| WINNER IS ||-----",winner)
        game_is_palying=False
    elif winner2 != None:
            winner = winner2
            print("-----|| WINNER IS ||-----", winner)
            game_is_palying = False
    elif winner3 != None:
            winner = winner3
            print("-----|| WINNER IS ||-----", winner)
            game_is_palying = False

def check_row():
    temp_row1 = b[0] == b[1] == b[2]!="-"
    temp_row2 = b[3] == b[4] == b[5]!="-"
    temp_row3 = b[6] == b[7] == b[8]!="-"
    if temp_row2 or temp_row1 or temp_row3:
        game_is_palying=False

    if temp_row1:
        return b[0]
    elif temp_row2:
        return b[3]
    elif temp_row3:
        return b[6]

def check_col():
    temp_col1 = b[0] == b[3] == b[6] != "-"
    temp_col2 = b[1] == b[4] == b[7] != "-"
    temp_col3 = b[2] == b[5] == b[8] != "-"
    if temp_col2 or temp_col1 or temp_col3:
        game_is_palying = False

    if temp_col1:
        return b[0]
    elif temp_col2:
        return b[1]
    elif temp_col3:
        return b[2]
def check_dia():
    temp_dia1 = b[0] == b[4] == b[8] != "-"
    temp_dia2 = b[2] == b[4] == b[6] != "-"

    if temp_dia2 or temp_dia1:
        game_is_palying = False

    if temp_dia1:
        return b[0]
    elif temp_dia2:
        return b[2]

def check_tie():
    global game_is_palying
    if "--" not in b:
        print("tied......")
        game_is_palying=False


def play_game():
    ch=input("do you want to play game[n\y]:")
    if ch=="y":
       while game_is_palying:
            display_board()
            handler()
            change_player()
            check_winner()
            check_tie()


    else:
            exit(0)



if game_is_palying==True:
        play_game()
else:
    print("over.....")
    exit(0)