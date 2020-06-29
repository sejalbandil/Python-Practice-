import numpy as np

#Function draw tic-tac-toe grid
def draw():
    x=0
    y=0
    while x<4:
        print(" --- --- ---")
        if y<3:
            print("| "+game[y][0]+" | "+game[y][1]+" | "+game[y][2]+" | ")
        x=x+1
        y=y+1


#Function to check winner from rows
def check_rows():
    for list in game:
        if list[0]==list[1]==list[2]=="X" or list[0]==list[1]==list[2]=="O":
        #if (list[0]==list[1]) and (list[0]==list[2]) and(list[0]=="X" or list[0]=="O")
            print("player "+list[0]+ " Won!")
            exit()


#Function to check winner from colums
def check_colums():
    numpy_game= np.transpose(game)

    for list in numpy_game:
        if list[0]==list[1]== list[2]=="X" or list[0]==list[1]== list[2]=="O":
            print("player "+list[0]+ " Won!")
            exit()

#Function to check winner from diagonal
def check_diagonal():
    if game[0][0]==game[1][1]==game[2][2]=="X" or game[0][0]==game[1][1]==game[2][2]=="O"  or game[0][2]==game[1][1]==game[2][0]=="X" or game[0][2]==game[1][1]==game[2][0]=="O":
        print("player "+game[1][1]+ " Won!")
        exit()

#Function to check a win:
def check_win():
    check_rows()
    check_colums()
    check_diagonal()

#Function to check repeat
def  check_repeat(r,c):
    if (r!= 1 or r!= 2 or r!= 3) and (c!= 1 or c!= 2 or c!= 3):
        print("Input Not Valid, Value Must Be Between 1-3")
        return 0
    if game[r][c]=="_":
        return 1

    print("Position Already Filled")
    return 0


game = [["_","_" ,"_" ],
	   ["_","_" ,"_" ],
	   ["_","_" ,"_" ]]

draw()
turn=1
while turn<10:

    if turn %2:
        player1_move= raw_input("Player One Make Your Move: ")
        row_col= player1_move.split(",")
        if check_repeat(int(row_col[0])-1,int(row_col[1])-1)==0:
            continue
        else:
            game[int(row_col[0])-1][int(row_col[1])-1]="X"

    else:
        player2_move= raw_input("Player Two Make Your Move: ")
        row_col= player2_move.split(",")
        if check_repeat(int(row_col[0])-1,int(row_col[1])-1)==0:
            continue
        else:
            game[int(row_col[0])-1][int(row_col[1])-1]="O"

    draw()
    check_win()

    turn=turn+1


print("TIE!")
