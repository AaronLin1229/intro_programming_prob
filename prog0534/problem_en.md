## Problem Description

Write a program to simulate Candy Crush. Find three adjacent repeated numbers in a $r$ by $c$ matrix and change them to zeros. For simplicity, your program only needs to find three repeated numbers in a row, in a column, or an L-shape pattern, and an integer will only appear at most three times in this matrix.

## Input Format

The first line has $r$ and $c$. Each of the following $r$ lines has $c$ integers as a row in the matrix.

## Output Format

There are $r$ lines in the output. Each of the $r$ lines has $c$ integers as a row in the matrix after setting adjacent repeated to zeros.

## Sample

```input1
4 3
1 1 1 
2 3 3
2 4 5
5 5 4
```

```output1
0 0 0 
2 3 3 
2 4 5 
5 5 4
```

```input2
3 4
1 1 2 3
2 5 3 3
2 4 5 5
```

```output2
1 1 2 0 
2 5 0 0 
2 4 5 5
```

```input3
4 4 
1 9 2 3
2 1 3 5
2 4 1 5
7 7 8 5
```

```output3
1 9 2 3 
2 1 3 0 
2 4 1 0 
7 7 8 0
```

```input4
6 5
1 1 1 2 2 
3 3 4 5 2
4 4 5 3 6 
7 7 15 8 8 
7 10 10 10 11 
12 12 12 13 13
```

```output4
0 0 0 0 0 
3 3 4 5 0 
4 4 5 3 6 
0 0 15 8 8 
0 0 0 0 11 
0 0 0 13 13
```

## Specification

- $1 \leq r, c \leq 500$

## Source

Judge Girl