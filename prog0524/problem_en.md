## Problem Description

Given two matrices $A$ and $B$, each of size $n \times m$, calculate the sum of these matrices, denoted as $A + B$. Matrix addition is defined as the addition of corresponding elements from the two matrices. That is, if $C = A + B$, then $C_{i,j} = A_{i,j} + B_{i,j}$ for all $1 \leq i \leq n$ and $1 \leq j \leq m$.

## Input Format

- The first line contains two space-separated integers $n$ and $m$, representing the number of rows and columns in the matrices, respectively.
- The next $n$ lines describe matrix $A$, with each line containing $m$ integers separated by spaces.
- The following $n$ lines describe matrix $B$, structured in the same way as matrix $A$.

## Output Format

Output $n$ lines, each containing $m$ integers separated by spaces, representing the matrix $C$ which is the sum of matrices $A$ and $B$.

## Sample
```input1
2 3
1 2 3
4 5 6
-1 -2 -3
-4 -5 -6
```

```output1
0 0 0
0 0 0
```

```input2
3 3
1 0 -1
2 0 2
-1 1 0
0 1 1
1 0 -1
0 -1 0
```

```output2
1 1 0
3 0 1
-1 0 0
```

## Specification

- $1 \leq n, m \leq 50$
- $-10 \leq A_{i,j}, B_{i,j} \leq 10$ for all $1 \leq i \leq n$ and $1 \leq j \leq m$
