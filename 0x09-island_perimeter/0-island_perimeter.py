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
    # validate grid dimensions
    rows = len(grid)
    if rows == 0:
        return 0
    cols = len(grid[0])
    if cols == 0:
        return 0
    if rows > 100 or cols > 100:
        return 0

    # Validate grid content
    island_count = 0
    for row in grid:
        if len(row) != cols:
            return 0
        for cell in row:
            if cell not in [0, 1]:
                return 0

    # Calculate the perimeter
    island_cell = 0
    flat_list = [num for row in grid for num in row]
    for cell in flat_list:
        if (cell == 1):
            island_cell += 1
    if (island_cell == 0):
        return 0
    perimeter = 2 * (island_cell + 1)
    return perimeter
