# [0. Rotate 2D Matrix](./0-rotate_2d_matrix/)

Given an n x n 2D matrix, rotate it 90 degrees clockwise.

* Prototype: `def rotate_2d_matrix(matrix):`
* Do not return anything. The matrix must be edited **in-place**.
* You can assume the matrix will have 2 dimensions and will not be empty.

```
jessevhedden$ cat main_0.py
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)

jessevhedden$
jessevhedden$ ./main_0.py
[[7, 4, 1],
[8, 5, 2],
[9, 6, 3]]
jessevhedden$
```

Logic:

* The matrix is rotated in place by swapping the values of the elements in the matrix.
1. First, I reverse the matrix by swapping the first row with the last row, the second row with the second to last row, etc.
so it comes out like this:
```
[[7, 8, 9],
[4, 5, 6],
[1, 2, 3]]
```
this can be done by calling simple reverse function on the matrix or slicing the matrix with a step of -1

2. Then, I swap the values of the elements (transpose) by iterating over the rows and using a nested loop to iterate over the columns.

3. a simultaneous swap is done by swapping the values of the elements in the matrix by their positions in the matrix.
```
(i, j) = (j, i)
```
 This effectively transposes the elements in the matrix and rotates it 90 degrees clockwise.

```
[[7, 4, 1],
[8, 5, 2],
[9, 6, 3]]
```