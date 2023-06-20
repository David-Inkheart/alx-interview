# Island Perimeter

This is a solution to the "Island Perimeter" problem.
The problem requires calculating the perimeter of an island described by a grid.
The grid consists of 0s representing water and 1s representing land cells.
The goal is to determine the perimeter of the island, considering specific
constraints mentioned in the problem description.

## Problem Description

Given a grid representing an island where:
- 0 represents water
- 1 represents land
- Each cell is square, with a side length of 1
- Cells are connected horizontally/vertically (not diagonally)
- The grid is rectangular, with its width and height not exceeding 100
- The grid is completely surrounded by water
- There is only one island (or nothing)
- The island doesn’t have “lakes” (water inside that isn’t connected to the
  water surrounding the island)

The task is to implement a function `island_perimeter(grid)`
that returns the perimeter of the island described in the grid.

## Solution

The solution provided here is a compact and efficient approach to solve the problem. The algorithm employed can be summarized as follows:

-  Iterate over each cell in the grid.
- If the cell value is 1, increment the perimeter count by 4.
- Check the adjacent cells (above and to the left) of the current cell.
  - If an adjacent cell is also a land cell, subtract 2 from the perimeter count to account for the shared side.
- Finally, return the calculated perimeter count.

The solution utilizes nested loops to iterate over each cell and performs constant time checks to calculate the perimeter.

## Usage

To use the solution, you can follow these steps:

1. Copy the `island_perimeter` function implementation from the provided code.
2. Call the `island_perimeter` function, passing the grid as an argument.
3. The function will return the perimeter of the island described in the grid.

Example usage:

grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(island_perimeter(grid))  # Output: 12

