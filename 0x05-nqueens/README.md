# 0x05. N Queens

## Tasks

### 0. N queens

The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.

- Usage: nqueens N
  - If the user called the program with the wrong number of arguments, print `Usage: nqueens N`, followed by a new line, and exit with the status `1`

- where N must be an integer greater or equal to `4`
    - If N is not an integer, print `N must be a number`, followed by a new line, and exit with the status `1`
    - If N is smaller than `4`, print `N must be at least 4`, followed by a new line, and exit with the status `1`

- The program should print every possible solution to the problem
    - One solution per line
    - Format: see example
    - You don’t have to print the solutions in a specific order

- You are only allowed to import the `sys` module

Read: [Queen](https://en.wikipedia.org/wiki/Queen_%28chess%29), [Backtracking](https://en.wikipedia.org/wiki/Backtracking)

```
julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
julien@ubuntu:~/0x08. N Queens$
```

LOGIC: [video sample for explananation](https://www.youtube.com/watch?v=xFv_Hl4B83A)

The objective of the `N-Queens` challenge is to find a valid configuration for the queens on the board, given the value of N. The problem becomes more complex as N increases because there are more potential positions for the queens, and it requires careful consideration to ensure they don't attack each other.

Various algorithms and techniques can be employed to solve the N-Queens problem. Some popular approaches include `backtracking`, `recursion`, and `constraint satisfaction algorithms`.

One common algorithm used to solve the N-Queens challenge is the `backtracking algorithm`. It works by systematically trying different positions for the queens and backtracking whenever a conflict is detected. By exploring different possibilities and discarding invalid configurations, the

This is an implementation of the N-Queens problem solver using a `backtracking algorithm`. Here's a breakdown of the algorithm and its complexities:

The `NQueensSolver class` initializes with the size of the board (N), creates an empty board, and sets up a list to store solutions.

The `solve` method initiates the solving process and returns the solutions. It calls the `place_queen` method to recursively place queens on the board.

The `place_queen` method is a recursive function that places queens column by column. It checks if it is safe to place a queen in a particular position using the `is_safe` method. If it's safe, it places the queen and moves on to the next column by calling itself recursively with `col + 1`. If it's not safe, it `backtracks` by removing the queen and continues checking other positions.

The `is_safe` method checks if a queen placed at a given row and column is safe from attacks by checking the `same row`, `upper diagonal`, and `lower diagonal` for any other queens. It returns True if it's safe and False otherwise.

The `get_queens` method retrieves the positions of the queens on the board and returns them as a list of coordinates based on their indices.

The `print_board` method prints the board, but it is not used in the current implementation. It was used to test queen positions.

The `main function` handles `command-line arguments`, `validates the input`, `creates an instance of NQueensSolver`, `solves the problem`, and `prints the solutions`.

Regarding complexities and possible optimizations:

`Time Complexity:` The backtracking algorithm has an exponential time c`omplexity of O(N!)`. It explores all possible configurations of queens on the board. As N increases, the number of possibilities grows rapidly.

`Space Complexity`: The space complexity of the current implementation is `O(N^2)` because it uses a `2D list: (List of lists)` to represent the board. Additionally, the solutions list stores all valid solutions, which can take up additional space.
