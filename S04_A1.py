import pyfiglet

def show():
    for row in game_board:
        for cell in row:
            print(cell, end="")
        print()



def check_game():

        if( game_board[0][0]=="o " and game_board[0][1]=="o " and game_board[0][2]=="o " or 
        game_board[1][0]=="o " and game_board[1][1]=="o " and game_board[1][2]=="o " or
        game_board[2][0]=="o " and game_board[2][1]=="o " and game_board[2][2]=="o " or
        game_board[2][0]=="o " and game_board[1][1]=="o " and game_board[0][2]=="o " or
        game_board[0][0]=="o " and game_board[1][1]=="o " and game_board[2][2]=="o "or
        game_board[0][0]=="o " and game_board[1][0]=="o " and game_board[2][0]=="o "or
        game_board[0][1]=="o " and game_board[1][1]=="o " and game_board[2][1]=="o "or
        game_board[0][2]=="o " and game_board[1][2]=="o " and game_board[2][2]=="o "):
            print("player 1 wins")
            exit(0)
                
        if( game_board[0][0]=="x " and game_board[0][1]=="x " and game_board[0][2]=="x " or 
        game_board[1][0]=="x " and game_board[1][1]=="x " and game_board[1][2]=="x " or
        game_board[2][0]=="x " and game_board[2][1]=="x " and game_board[2][2]=="x " or
        game_board[2][0]=="x " and game_board[1][1]=="x "  and game_board[0][2]=="x " or
        game_board[0][0]=="x " and game_board[1][1]=="x " and game_board[2][2]=="x "or
        game_board[0][0]=="x " and game_board[1][0]=="x " and game_board[2][0]=="x "or
        game_board[0][1]=="x " and game_board[1][1]=="x " and game_board[2][1]=="x "or
        game_board[0][2]=="x " and game_board[1][2]=="x " and game_board[2][2]=="x "):
            print("player 2 wins")
            exit(0)
    

 
 
    

title = pyfiglet.figlet_format("Tic Tac Toe", font = "slant")
print(title)

game_board = [["- ", "- ", "- "],
              ["- ", "- ", "- "],
              ["- ", "- ", "- "]]

show()
    
while True:   
    print("Pleayer 2")
    while True:
        row = int(input())
        col = int(input())
        if 0 <= row <= 2 and 0 <= col <= 2:
            if game_board[row][col] == "- ":
                game_board[row][col] = "o "
                show()
                check_game()
                break
            else:
                print("select another cell")
        else:
            print("Enter the number between 0 and 2")
            
    print("Pleayer 1")
    while True:
        row = int(input())
        col = int(input())
        if 0 <= row <= 2 and 0 <= col <= 2:
            if game_board[row][col] == "- ":
                game_board[row][col] = "x "
                show()
                check_game()
                break
            else:
                print("select another cell")
        else:
            print("Enter the number between 0 and 2")
            
        

    