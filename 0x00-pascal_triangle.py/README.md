## [0. Pascal's Triangle](./0-pascal_triangle.py)

### Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:

- Returns an empty list if n <= 0
- You can assume n will be always an integer

```
guillaume@ubuntu:~/0x00$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

guillaume@ubuntu:~/0x00$ 
guillaume@ubuntu:~/0x00$ ./0-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
guillaume@ubuntu:~/0x00$ 
```

### Major concept learned: 

- ["binomial coefficient"](https://en.wikipedia.org/wiki/Binomial_coefficient) or the "combinations" formula. The binomial coefficient expresses the number of ways that `a` objects can be chosen from a set of `b` objects, and it is used extensively in combinatorics and probability theory.

- In the context of the [Pascal's triangle](https://en.wikipedia.org/wiki/Pascal%27s_triangle), the binomial coefficient formula states that the value of the `j-th element` in the `i-th row` is equal to the sum of the `(j-1)-th and j-th` elements in the `(i-1)-th row`. This is because choosing `a` objects from a set of `b` objects can be done by either including or excluding the `a-th` object, so the total number of ways to choose `a` objects is equal to the number of ways to choose `a-1` objects plus the number of ways to choose `a` objects without including the `a-th` object. This relationship is captured by the addition of the two values from the previous row in the Pascal's triangle.

For example, In my solution:
```
row.append(triangle[idx - 1][j - 1] + triangle[idx - 1][j])
```
1. `triangle[idx - 1]` retrieves the `idx-1-th row` of the Pascal's triangle. Since Python uses 0-based indexing, the first row is at index 0, the second row is at index 1, and so on.

2. `triangle[idx - 1][j - 1]` retrieves the `(idx-1)-th row` and `(j-1)-th element` of the Pascal's triangle. This is because the first and last element of each row is always 1, so we only need to calculate the values in between.

3. `triangle[idx - 1][j]` retrieves the `(idx-1)-th row` and `j-th element` of the Pascal's triangle.

4. `triangle[idx - 1][j - 1] + triangle[idx - 1][j]` adds the two values together(of the same previous row[idx -1]), which gives us the value for the `j-th element` of the `idx-th row`(current row) of the Pascal's triangle.

5. `row.append(triangle[idx - 1][j - 1] + triangle[idx - 1][j])` adds this calculated value to the row list for the `idx-th row`.

So basically, this line retrieves the two values needed to calculate the current value of the Pascal's triangle, adds them together, and appends the result to the current row being constructed, and this is a popular `combinatorial` concept.