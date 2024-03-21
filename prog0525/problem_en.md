## Problem Description

Given two matrices, $A$ (of size $n \times m$) and $B$ (of size $m \times k$), your task is to compute their matrix product and print it out. The matrix multiplication of $A$ and $B$ is defined as follows:

- The resulting matrix, $C$, will be of size $n \times k$.
- Each element $C_{ij}$ in the matrix $C$ is calculated as the sum of the products of corresponding elements from the $i^{th}$ row of $A$ and the $j^{th}$ column of $B$.

That is, $C_{ij} = \sum_{r=1}^{m} A_{ir} \cdot B_{rj}$.

## Input Format

- The first line contains three integers $n$, $m$, and $k$, representing the dimensions of matrices $A$ and $B$.
- The next $n$ lines each contain $m$ integers, representing the rows of matrix $A$.
- The following $m$ lines each contain $k$ integers, representing the rows of matrix $B$.

## Output Format

Output $n$ lines, each containing $k$ integers, representing the rows of the matrix $C$, the product of $A$ and $B$.

## Sample

```input1
2 3 2
1 0 2
-1 3 1
3 1
2 1
1 0
```

```output1
5 1
4 2
```

```input2
3 2 3
1 2
3 4
5 6
1 1 1
2 2 2
```

```output2
5 5 5
11 11 11
17 17 17
```

## Specification

- $1 \leq n, m, k \leq 50$
- $-10 \leq$ All entries in matrices $A$ and $B$ $\leq 10$
