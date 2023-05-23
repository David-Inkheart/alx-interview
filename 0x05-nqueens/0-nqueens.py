#!/usr/bin/python3
"""
# let the n-queens problem be defined as follows:
    - given an N x N chessboard, place N queens on the board such
    that no queen can attack another queen
    - a queen can attack another queen if they are on the same
    row, column, or diagonal

# Questions:
    - what is the input?
        - an integer n supplied on the command line as an
        argument to this script
    - what is the output?
        - a list of lists of integers representing the column and
        row positions of the queens on the board
    - what are some constraints?
        - If the user called the program with the wrong number of
        arguments, print `Usage: nqueens N`, followed by a new
        line, and exit with the status 1
        - where N must be an integer greater or equal to 4
        - If N is not an integer, print `N must be a number`,
        followed by a new line, and exit with the status 1
        - If N is smaller than 4, print `N must be at least 4`,
        followed by a new line, and exit with the status 1
        - if no solution exists, return an empty list

# examples:
    - N = 4
        - [[0 ,1], [1, 3], [2, 0], [3, 2]]
        - [[0 ,2], [1, 0], [2, 3], [3, 1]]
    - N = 6
        - [[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
        - [[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
        - [[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
        - [[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]

# Approach:
    - backtracking algorithm (recursive) with pruning (is_safe)
    - and memoization (board) techniques to reduce time
      complexity and space complexity respectively (see below)

# Complexity:
    - time complexity: O(n!)
    - space complexity: O(n^2)

# Comments:
    - use echo $? to see the exit status of the last command

"""

import sys


class NQueensSolver:
    """NQueensSolver class that solves the n-queens problem"""

    def __init__(self, N):
        """initialize the NQueensSolver class"""
        self.n = N
        self.board = [[0 for col in range(N)] for row in range(N)]
        self.solutions = []

    def solve(self):
        """solve the n-queens problem and return the solutions"""
        self.place_queen(0)
        return self.solutions

    def place_queen(self, col):
        """place the queens on the board"""
        if col == self.n:
            self.solutions.append(self.get_queens())
            return True
        # for each row in the column
        for row in range(self.n):
            if self.is_safe(row, col):
                self.board[row][col] = 1
                self.place_queen(col + 1)
                self.board[row][col] = 0

    def is_safe(self, row, col):
        """check if the queen is safe to place in the given
        position"""
        for c in range(col):
            if self.board[row][c] == 1:
                return False
        # check upper diagonal
        for r, c in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[r][c] == 1:
                return False
        # check lower diagonal
        for r, c in zip(range(row, self.n), range(col, -1, -1)):
            if self.board[r][c] == 1:
                return False

        return True

    def get_queens(self):
        """get the queens on the board"""
        queens = []
        for row in range(self.n):
            for col in range(self.n):
                if self.board[row][col] == 1:
                    queens.append([row, col])
        return queens

    # def print_board(self):
    #     """print the board"""
    #     for row in self.board:
    #         print(row)


def main():
    """main function dealing with the constraints"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    n_queens = NQueensSolver(n)
    solutions = n_queens.solve()
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    """call main function"""
    main()
