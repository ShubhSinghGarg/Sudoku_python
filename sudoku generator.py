
#functions and procedures to generate an sudoku board with a unique solution

import random
import pprint

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

random.seed(None)

def generator(grid):
    difficultySelector(grid)

    return grid

def difficultySelector(grid):

    print(" \n What level of challenge would you like to tackle: ")
    print("\n \t 1. Easy")
    print("\n \t 2. Medium")
    print("\n \t 3. Hard")

    clues = 0
    difficulty = int(input("Enter the difficulty: "))

    if difficulty == 1:
        clues = 40
    elif difficulty == 2:
        clues = 27
    elif difficulty == 3:
        clues = 17
    else:
        print("Plese select a difficulty 1-3")

    print(clues)
    for x in range(0, clues):
        filler(grid)

def filler(grid):

    row = random.randint(0,8)
    col = random.randint(0,8)

    ins = random.randint(1, 9)

    if grid[row][col] == 0 and valid_filler(grid, (row, col), ins):
        print(1)
        grid[row][col] = ins
    else:
        print(2)
        filler(grid)

#checks to see if the made move is valid
def valid_filler(board, position, num):

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

printer = pprint.PrettyPrinter(width = 41, compact = True)
generator(grid)
printer.pprint(grid)
