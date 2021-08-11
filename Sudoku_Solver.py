import time

iterations = 0

# Simple program in Python to solve a Sudoku puzzle using Recursion and backtracking
 
# Format and display the Sudoku puzzle familiar to the end user
def display(sudoku):
    print("\n+-----------------------+")
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("|-------+-------+-------|")

        for j in range(9):
            if j % 3 == 0:
                print("| ", end="")

            if j == 8:
                print(f"{sudoku[i][j]} |")
            else:
                print(f"{sudoku[i][j]} ", end="")
    print("+-----------------------+\n")
 
# Check to see if the row, column or sub-box already contains the number thats being added.
def possible(row, col, num):
    
    # Check columns for a duplicate
    for i in range(9):
        if sudoku[row][i] == num:
            return False
    
    # Check rows for a duplicate
    for i in range(9):
        if sudoku[i][col] == num:
            return False

    # Using floor division operator(//) round down to the nearest int and multiply by 3
    # This creates a 3x3 grid of sub-boxes
    subbox_row = (row//3)*3
    subbox_col = (col//3)*3

    # Iterate through the 3x3 grid checking if the number already exists
    for i in range(3):
        for j in range(3):
            if sudoku[i + subbox_row][j + subbox_col] == num:
                return False

    return True
 
# The solve function will add a value (1-9) into an empty cell and use backtracking
# if future entries are not successful due to this entry.
def solve(sudoku, row, col):
    global iterations
    iterations += 1

    # We could create a function to programmatically get the X/Y axis of the next empty 
    # cell, but this would require us to iterate through the grid unnecessarily.
    # Because the Sudoku grid is static, its faster to manually set the values.

    # End of puzzle, nothing left to do
    if (row == 8 and col == 9):
	    return True
	
	# End of column, move to the beginning of the next row
    if col == 9: row += 1; col = 0

	# RECURSION
    # Check if the current cell already contains a number, if so, iterate to the next column
    if sudoku[row][col] > 0:
	    return solve(sudoku, row, col + 1)

    # if the value does not exist horizontally, vertically or in the subbox add it
    for num in range(1,10):  
        if possible(row, col, num):
            sudoku[row][col] = num

            # Attempt worked, move to the next cell         
            if solve(sudoku, row, col + 1):
                return True
            
            # Attempted failed, reset to 0 and try the next number
            sudoku[row][col] = 0 

    # This triggers the backtracking where the next number will be chosen
    # and attempted in the previous cell
    return False

# assigning values to the puzzle
sudoku = [
        [0, 0, 4, 0, 0, 0, 0, 7, 0],
		[5, 0, 0, 0, 0, 6, 0, 0, 0],
		[0, 0, 0, 5, 0, 0, 0, 0, 3],
		[0, 3, 0, 0, 0, 0, 7, 0, 0],
		[0, 0, 0, 0, 6, 0, 0, 0, 0],
		[0, 0, 1, 0, 0, 0, 0, 2, 0],
		[2, 0, 0, 0, 0, 7, 0, 0, 0],
		[0, 0, 0, 2, 0, 0, 0, 0, 5],
		[0, 6, 0, 0, 0, 0, 2, 0, 0]
        ]
     
start = time.time()     

# if successful, print
if(solve(sudoku, 0, 0)):
    display(sudoku)
else:
    print("No solution exists")

stop = time.time()
print(f"Number of attempts: {iterations} in {round(stop-start, 4)} seconds")