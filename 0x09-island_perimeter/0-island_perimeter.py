#!/usr/bin/python3
def island_perimeter(grid):
    perimeter = 0
    
    rows = len(grid)
    cols = len(grid[0])
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with 4 sides for each land cell
                perimeter += 4
                
                # Check the cell above (i-1, j)
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 1
                
                # Check the cell below (i+1, j)
                if i < rows - 1 and grid[i+1][j] == 1:
                    perimeter -= 1
                
                # Check the cell to the left (i, j-1)
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 1
                
                # Check the cell to the right (i, j+1)
                if j < cols - 1 and grid[i][j+1] == 1:
                    perimeter -= 1
    
    return perimeter
