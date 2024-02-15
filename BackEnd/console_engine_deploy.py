"""
  ____                      _        _____             _            
 / ___|___  _ __  ___  ___ | | ___  | ____|_ __   __ _(_)_ __   ___ 
| |   / _ \| '_ \/ __|/ _ \| |/ _ \ |  _| | '_ \ / _` | | '_ \ / _ \
| |__| (_) | | | \__ \ (_) | |  __/ | |___| | | | (_| | | | | |  __/
 \____\___/|_| |_|___/\___/|_|\___| |_____|_| |_|\__, |_|_| |_|\___|
                                                 |___/              

"""

#CONSOLE ENGINE NONOGRAM
import random


def create_nonogram(rows, columns, max_sequential_val):
    # Create an empty board matrix
    grid = [[0 for _ in range(columns)] for _ in range(rows)]

    print("--Matrix created--")
    for i in grid:
        print(i)

    # Init hints for rows and columns
    row_hints = []
    col_hints = []

    #Generate random row values bw 0/1 and add them to the hints
    #Iterate inside the grid and randomly generate the field
    for i in range(rows):

        #Continuous variable tracking the generator
        temp= 0 
        #Local var hints list
        hint = []

        #Loop inside the columns for hints and assign grid values
        for j in range(columns):
            # Randomly decide if the square should be colored or not
            if random.random() > 0.5: #If random [0,1) is closer to 1 than temp rises 
                grid[i][j] = 1 #[row_range][col_range] set the black box state
                temp += 1
            else:
                #Check if the temp is positive and add it to the local hint
                if temp > 0: 
                    hint.append(temp)
                    temp = 0 #zanuli
        if temp > 0:
            hint.append(temp)
        row_hints.append(hint)

    #Check if some value through the matrix is 1 and increase the temp variable to append it to the col hint 
    for j in range(columns):
        temp = 0
        hint = []
        for i in range(rows):
            if grid[i][j] == 1:
                temp += 1
            else:
                if temp > 0:
                    hint.append(temp)
                    temp = 0
        if temp > 0:
            hint.append(temp)
        col_hints.append(hint)
        

    print("--Updated--")

    
    # By shortening the hints to a limited length acourding to max_sequential_val, 
    # the code ensures that the hints provided to the player will not be too long and difficult to understand, 
    # making the game more manageable and enjoyable.
    for i in range(len(row_hints)):
        row_hints[i] = row_hints[i][:max_sequential_val]
    for i in range(len(col_hints)):
        col_hints[i] = col_hints[i][:max_sequential_val]
    
    #Spit out the game board
    return (grid, row_hints, col_hints)


def generate_grid():
    
    print("Board:")
    for i in range(rows):
        print(grid[i])
    # print cols/rows hints
    print("   Col hints:", col_hints)
    for i in row_hints:
        print("Row hint" + str(i) + "\n")

#IMPLEMENTATION STATES
generate = True
if generate:
    # Choose the size of the matrix and config the sequential value as needed (for 5 and 6x scale you can keep it at 3 values at max)
    rows, columns, max_sequential_val = 5, 5, 3
    puzzle = create_nonogram(rows, columns, max_sequential_val)
    #tuple unpacking to assign the values returned from the function "create_nonogram" to three separate variables
    grid, row_hints, col_hints = puzzle
    generate_grid()
else: print('False')










