## Problem Description

In a mystical orchard, there are dragon fruit trees arranged in an $n \times m$ matrix. Each tree in the orchard has a specific number of dragon fruits on it, denoted as $A_{ij}$, where $i$ and $j$ represent the row and column of the tree, respectively.

A mischievous lizard lives in this orchard. It has developed a unique way of feasting on these fruits. The lizard can climb any tree and consume all the dragon fruits from the eight surrounding trees (if they exist) and the tree it has climbed on. The goal is to determine the maximum number of dragon fruits the lizard can consume by climbing a single tree and to identify the index of that tree. If there are multiple trees offering the same maximum number, the tree with the least dictionary order (smallest row and then column index) should be chosen.

## Input Format

- The first line contains two integers, $n$ and $m$, representing the dimensions of the matrix.
- The next $n$ lines each contain $m$ integers. The $j$-th integer in the $i$-th line represents $A_{ij}$, the number of dragon fruits on the tree located at position $(i, j)$.

## Output Format

- The first line should be a single number, the maximum number of dragon fruits the lizard can consume.
- The second line should be two numbers seperated by space, the position (index) of the maximum number of dragon fruits is achieved.

Note: the index system should be 0-indexed in this problem.

## Sample

```input1
9 3
12 42 55
11 38 55
36 64 92
76 11 14
35 46 81
85 100 84
64 10 47
75 1 19
66 91 37
```

```output1
552
5 1
```

```input2
1 10
76 51 64 9 58 69 5 33 28 74
```

```output2
191
0 1
```

## Specification

- $1 \leq n, m \leq 12$
- $0 \leq A_{ij} \leq 100$
