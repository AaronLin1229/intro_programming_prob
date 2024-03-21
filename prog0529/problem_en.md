## Problem Description

Suppose we have an $N$ by $N$ grid, $G$ like the following.

![img](file://1.png)

If we go from the center of the matrix and enumerate the elements in clockwise spiral order, we will have a vector of elements like the following.

![img](file://2.png)

Now given the snake array, we would like to construct the original matrix $G$, then put the elements back into a result array in a row by row, column by column manner, like the following.

![img](file://3.png)

## Input Format

Input contains one test case, each test case has 2 lines.

The first line in the test case contains one integer, $N$, meaning the matrix size is $N$ by $N$. Then next line contains $N^2$ integers indicating the elements of the snake.

## Output Format

Print out the result.

## Sample

```input1
3
1 2 3 4 5 6 7 8 9
```

```output1
3 4 5 2 1 6 9 8 7
```

```input2
3
6 8 10 9 16 15 18 23 29
```

```output2
10 9 16 8 6 15 29 23 18
```

## Specification

- $N$ is odd and $1 \leq N \leq 99$

## Source

Judge Girl
