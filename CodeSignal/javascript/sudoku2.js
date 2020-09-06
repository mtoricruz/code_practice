// Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with numbers in such a way that each column, each row, 
// and each of the nine 3 × 3 sub-grids that compose the grid all contain all of the numbers from 1 to 9 one time.

// Implement an algorithm that will check whether the given grid of numbers represents a valid Sudoku puzzle according to the layout rules described above. 
// Note that the puzzle represented by grid does not have to be solvable.

// U
// basic rules of sudoku
// no number should appear on same row/col more than once
// implement an algo to check if numbers on grid rep a valid puzzle
// if valid return true else return false

// P
// traverse through grid
// check if row/col have unique integers 
// if valid return true else return false


sudoku = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
          ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
          ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
          ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
          ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
          ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
          ['.', '.', '.', '5', '.', '.', '.', '7', '.']]

// E
function sudoku2(grid) {
    for(var row = 0; row < 9; row++){
        for(var col = 0; col < 9; col++){
            if(grid[row][col] == grid[col][row]){
                return true
            } else {
                return false
            }
        }
    }
}

console.log(sudoku2(sudoku))

// R
// 