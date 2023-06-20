#!/usr/bin/python3
"""
returns the perimeter of the island described in grid
--grid is a list of list of integers:
-----0 represents water
-----1 represents land
-----Each cell is square, with a side length of 1
-----Cells are connected horizontally/vertically (not diagonally).
-----grid is rectangular, with its width and height not exceeding 100
--The grid is completely surrounded by water
--There is only one island (or nothing).
--The island doesn’t have “lakes” (water inside that isn’t connected to the
-----water surrounding the island).
"""


def island_perimeter(grid):
    """
    Returns perimeter of the island described in grid
    """
    # Validate grid dimensions and content
    rows = len(grid)
    if rows == 0:
        return 0
    cols = len(grid[0])
    if cols == 0:
        return 0
    if rows > 100 or cols > 100:
        return 0
    perimeter = sum(
        4
        - (i > 0 and grid[i - 1][j] == 1)
        - (j > 0 and grid[i][j - 1] == 1)
        - (i < rows - 1 and grid[i + 1][j] == 1)
        - (j < cols - 1 and grid[i][j + 1] == 1)
        for i in range(rows)
        for j in range(cols)
        if grid[i][j] == 1
    )

    return perimeter
