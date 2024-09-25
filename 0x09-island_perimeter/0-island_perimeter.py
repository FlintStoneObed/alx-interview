#!/usr/bin/python3
"""
This module defines the island_perimeter function.
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid.

    Args:
        grid (list of list of int): A list of lists where 0 represents water 
                                    and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with a cell having 4 potential edges
                perimeter += 4

                # Check if there is land above the current cell
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

                # Check if there is land to the left of the current cell
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter

