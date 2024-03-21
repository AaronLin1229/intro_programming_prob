## Problem Description

Given a matrix of size $n \times m$, your task is to rotate the matrix by 90 degrees in a clockwise direction. The matrix will consist of integers.

## Input Format

The first line contains two space-separated integers $n$ and $m$, representing the number of rows and columns of the matrix, respectively. 
The next $n$ lines each contain $m$ space-separated integers, representing the elements of the matrix.

## Output Format

Output the rotated matrix. Each line should contain $m$ space-separated integers.

## Sample

```input1
3 3
1 2 3
4 5 6
7 8 9
```

```output1
7 4 1
8 5 2
9 6 3
```

```input2
4 3
1 2 3
4 5 6
7 8 9
10 11 12
```

```output2
10 7 4 1
11 8 5 2
12 9 6 3
```

## Specification

- $1 \leq n, m \leq 1000$
- Each element in the matrix is an integer.
