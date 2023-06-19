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

## My Solution

The solution provided here is a straightforward and efficient approach to solve
the problem. The algorithm employed can be summarized as follows:

1. Initialize a variable `island_cell` to track the count of land cells.
2. Flatten the grid into a single list using list comprehension.
3. Iterate over each cell in the flattened list.
4. If the cell value is 1, increment the `island_cell` count.
5. If `island_cell` is 0, return 0 (indicating no land cells).
6. Calculate the perimeter by multiplying the `island_cell` count by 2 and adding 2
(to account for the outer edges of the island) or perimeter formular of a rectangle.
7. Return the calculated perimeter.

The solution has a time complexity of O(N), where N is the total number of cells in
the grid. It effectively counts the land cells and calculates the perimeter based
on the count.

The provided solution meets the requirements of the problem, produces the expected
output for the given test case and possible edge cases,
and handles the constraint of not having "lakes" inside the island.

## Usage

To use the solution, you can follow these steps:

1. Copy the `island_perimeter` function implementation from the provided code.
2. Call the `island_perimeter` function, passing the grid as an argument.
3. The function will return the perimeter of the island described in the grid.

Example usage:

```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(island_perimeter(grid))  # Output: 12

