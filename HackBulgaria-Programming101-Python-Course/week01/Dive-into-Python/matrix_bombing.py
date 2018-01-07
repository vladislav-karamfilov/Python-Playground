"""
You are given a NxM matrix of integer numbers. We can drop a bomb at any place in the matrix, which has the
following effect:
- All of the 3 to 8 neighbours (depending on where you hit!) of the target are reduced by the value of the target.
- Numbers can be reduced only to 0 - they cannot go to negative.

For example, if we have the following matrix:
10 10 10
10  9  10
10 10 10
and we drop bomb at 9, this will result in the following matrix:
1 1 1
1 9 1
1 1 1

Implement a function called matrix_bombing_plan(m). The function should return a dictionary where keys are
positions in the matrix, represented as tuples, and values are the total sum of the elements of the matrix,
after the bombing at that position. The positions are the standard indexes, starting from (0, 0).

For example if we have the following matrix:
1 2 3
4 5 6
7 8 9

and run the function, we will have:
{(0, 0): 42,
 (0, 1): 36,
 (0, 2): 37,
 (1, 0): 30,
 (1, 1): 15,
 (1, 2): 23,
 (2, 0): 29,
 (2, 1): 15,
 (2, 2): 26}

We can see that if we drop the bomb at (1, 1) or (2, 1), we will do the most damage!
"""

from pprint import pprint as pp
from sum_of_numbers_in_matrix import sum_matrix


def matrix_bombing_plan(matrix):
    bombing_plan = {}

    rows = len(matrix)
    if rows == 0:
        return matrix_bombing_plan

    columns = len(matrix[0])
    for i in range(rows):
        for j in range(columns):
            bombed_matrix = _bomb_matrix(matrix, i, j, rows, columns)

            bombing_plan[(i, j)] = sum_matrix(bombed_matrix)

    return bombing_plan


def _bomb_matrix(matrix, i, j, rows, columns):
    neighbours_coordinates = _get_neighbours_coordinates(i, j, rows, columns)
    bombed_matrix = _update_neighbours(matrix, neighbours_coordinates, i, j, rows, columns)

    return bombed_matrix


def _get_neighbours_coordinates(i, j, rows, columns):
    neighbours_coordinates = set()

    # Up left
    if i > 0 and j > 0:
        neighbours_coordinates.add((i - 1, j - 1))

    # Up
    if i > 0:
        neighbours_coordinates.add((i - 1, j))

    # Up right
    if i > 0 and j < columns - 1:
        neighbours_coordinates.add((i - 1, j + 1))

    # Left
    if j > 0:
        neighbours_coordinates.add((i, j - 1))

    # Right
    if j < columns - 1:
        neighbours_coordinates.add((i, j + 1))

    # Down left
    if i < rows - 1 and j > 0:
        neighbours_coordinates.add((i + 1, j - 1))

    # Down
    if i < rows - 1:
        neighbours_coordinates.add((i + 1, j))

    # Down right
    if i < rows - 1 and j < columns - 1:
        neighbours_coordinates.add((i + 1, j + 1))

    return neighbours_coordinates


def _update_neighbours(matrix, neighbours_coordinates, i, j, rows, columns):
    bombed_matrix = [[] for _ in range(0, rows)]
    for x in range(rows):
        bombed_matrix[x] = [[] for _ in range(0, columns)]
        for y in range(columns):
            if (x, y) in neighbours_coordinates:
                if matrix[x][y] > matrix[i][j]:
                    bombed_matrix[x][y] = matrix[x][y] - matrix[i][j]
                else:
                    bombed_matrix[x][y] = 0
            else:
                bombed_matrix[x][y] = matrix[x][y]

    return bombed_matrix


def main():
    print('***Matrix Bombing Plan***')
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    pp(matrix_bombing_plan(matrix))


if __name__ == '__main__':
    main()
