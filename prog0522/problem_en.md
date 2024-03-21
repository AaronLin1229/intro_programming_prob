## Problem Description

In linear algebra, the transpose of a matrix is an operation that flips a matrix over its diagonal, switching the matrix's row and column indices. This problem involves writing a program to transpose a given $n \times m$ matrix.

Given a matrix $A$ of dimensions $n \times m$, where $n$ represents the number of rows and $m$ the number of columns, your task is to compute the transpose of $A$. The transpose of the matrix $A$, denoted as $A^T$, is a matrix of dimensions $m \times n$ where each element $A^T_{ij} = A_{ji}$.

## Input Format

- The first line contains two integers $n$ and $m$, representing the number of rows and columns of the matrix $A$, respectively.
- The next $n$ lines each contain $m$ integers, representing the elements of the matrix $A$.

## Output Format

- Output $m$ lines, each containing $n$ integers. These lines represent the transposed matrix $A^T$.

## Sample

```input1
2 3
1 2 3
4 5 6
```

```output1
1 4
2 5
3 6
```

```input2
3 2
7 8
9 10
11 12
```

```output2
7 9 11
8 10 12
```

## Specification

- $1 \leq n, m \leq 1000$
- Each element of the matrix $A$ is an integer in the range $-10^9 \leq A_{ij} \leq 10^9$.
