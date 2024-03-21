## Problem Description

Write a program that reads the dimensions (number of rows $r$ and columns $c$) of a two-dimensional integer array $A$. Then, read the array elements row by row. Your task is to find and print the elements of $A$ that are greater than all of their neighbors. An element in $A$ can have at most 4 neighbors (above, below, left, right). If there are multiple such elements, print them in the order of their appearance in the array, row by row, and column by column.

## Input Format

The first line contains two integers, $r$ and $c$, separated by a space, representing the number of rows and columns of the array respectively.
The next $r$ lines each contain $c$ integers, representing the elements of the array $A$.

## Output Format

Print the elements that are greater than all of their neighbors, in the order they appear in the array, each on a new line.

## Sample

```input1
3 3
1 2 3
4 5 6
7 8 9
```

```output1
9
```

```input2
2 3
7 8 3
4 5 6
```

```output2
8
6
```

## Specification

- $1 \leq r, c \leq 100$
- $-10^9 \leq A_{i,j} \leq 10^9$ for $1 \leq i \leq r$ and $1 \leq j \leq c$.

## Source

Judge Girl