#           line[i]
#              v
g =    [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]


def check_unique(nums):
    # create empty set to add num values in
    s = set()
    # loop through each item in line 
    for num in nums:
        # if box is 'empty' continue
        if num == '.':
            continue
        # if num is in set already 
        if num in s:
            # it is not unique
            return False
        # otherwise add num to set
        s.add(num)
    # return True if each num is unique in line
    return True

def sudoku2(grid):
    # loop thru each row in grid
    for line in grid:
        # check if each number in row is unique 
        if not check_unique(line):
            return False
    # loop through each item in col
    for i in range(9):
        # line[i] is each column of line in grid
        if not check_unique([line[i] for line in grid]):
            return False
    # loop through each sudoku box (3x3) to see if unique
    # for row of 3
    for i in range(0,9, 3):
        # for col of 3
        for j in range(0, 9, 3):
            # check if each box has unique integers
            if not check_unique(grid[i][j:j+3] + grid[i+1][j:j+3] + grid[i+2][j:j+3]):
                return False
    return True

print(sudoku2(g))