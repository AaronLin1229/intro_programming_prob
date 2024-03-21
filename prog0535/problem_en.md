## Problem Description

Write a program to find the maximum sum of a diamond shape in a $h \times w$ matrix. The following figure illustrates a diamond of size 3.

![img](file://1.jpeg)

## Input Format

The first line has $h$, $w$ and $k$. $k$ is no less than $3$, and $h$ and $w$ are large enough to contain at least a diamond. Each of the next $h$ lines has $w$ positive integers as a row in the matrix. The int data type is sufficient for all arithmetics without overflow.

## Output Format

The output has the maximum sum of elements in a diamond of size $k$.

## Sample

```input1
5 6 3
1 2 3 4 5 6
1 2 3 4 5 6
1 2 3 4 5 6
1 2 3 4 5 6
1 2 3 4 5 6
```

```output1
32
```

## Specification

- 20 pts: $k = 3, h \leq 50, w \leq 50$
- 80 pts: $3 \leq k \leq 50, h \leq 200, w \leq 200$

## Source

Judge Girl