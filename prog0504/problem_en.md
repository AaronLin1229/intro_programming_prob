## Problem Description

Write a program to count the number of integers which can be written as $M \cdot k, M \cdot k + 1, \dots, M \cdot k + (M - 1)$ respectively.

## Input Format

The first line has the number of input integers $N$. Each of the following $N$ lines has an input integer. The last line has $M$.

## Output Format

The number of integers which can be written as $M \cdot k, M \cdot k + 1, \dots, M \cdot k + (M - 1)$.

## Sample

```input1
5
1
2
3
4
5
3
```

```output1
1
2
2
```

```input2
10
3
1
4
1
5
9
2
6
5
3
3
```

```output2
4
3
3
```

## Specification

- $1 \leq N \leq 10^5$
- $1 \leq M \leq 2 \times 10^5$
- All numbers are in `int`.

## Source

Judge Girl