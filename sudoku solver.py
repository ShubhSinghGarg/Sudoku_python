
import pprint

#populate thhis board to be solved
grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

def board_input():
    
    print("\n Would you like to enter the board, or is it already populated:")
    print("\n\t 1. Enter the board")
    print("\n\t 2. Already populated")

    choice = int(input("\n Please enter your choice: "))

    if choice == 1:
        user_board(grid)
    

def user_board(board):

    print("\n please start entering the board (Enter 0 for empty space) :-")

    for i in range(0, 9):
        print("---------------------------------------------------")
        for j in range(0, 9):
            val = int(input("please enter the element for (" + str(i+1) + ", " + str(j+1) + ") :"))
            board[i][j] = val
        
        print("\n")

#The driver function to populate the sudoku board
def solve(board):

    find = find_empty(board)
    if find:
        row, col = find
    else:
        return True

    for i in range(1,10):
        if valid(board, (row, col), i):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

#checks to see if the made move is valid
def valid(board, position, num):

    #checks the row
    for i in range(0, len(board)):
        if  board[position[0]][i] == num and position[1] != i:
            return False

    #checks the column
    for i in range(0, len(board)):
        if board[i][position[1]] == num and position[1] != i:
            return False


    #check box

    box_x = position[1]//3
    box_y = position[0]//3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i, j) != position:
                return False

    return True

#finds a blank space in the board
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

    return None

#displays the completeed board
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("*******************************")
        for j in range(len(board[0])):
            if j % 3 == 0:
                print(" | ", end = "")
            if j == 8:
                print(board[i][j], end = "\n")
            else:
                print(str(board[i][j]) + " ", end = "")

    print("//////////////////////////////////////////////////////////")


board_input()
solve(grid)

print_board(grid)
