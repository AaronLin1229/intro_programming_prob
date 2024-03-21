## Problem Description

Given a $n \times m$ matrix $A$, your task is to find the maximum value in each row and the minimum value in each column of the matrix.

## Input Format

The first line contains two integers $n$ and $m$, representing the number of rows and columns of the matrix $A$, respectively.
The next $n$ lines each contain $m$ integers, describing the matrix $A$.

## Output Format

Output two lines.
The first line should contain $n$ integers, where the $i$-th integer is the maximum value in the $i$-th row of matrix $A$.
The second line should contain $m$ integers, where the $j$-th integer is the minimum value in the $j$-th column of matrix $A$.

## Sample

```input1
3 4
1 2 3 4
5 6 7 8
9 10 11 12
```

```output1
4 8 12
1 2 3 4
```

```input2
2 2
10 20
30 40
```

```output2
20 40
10 30
```

## Specification

- $n$: $1 \leq n, m \leq 1000$
- $m$: $1 \leq m \leq 1000$
- $-10^6 \leq A_{i,j} \leq 10^6$
