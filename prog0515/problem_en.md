## Problem Description

Given two sorted arrays, $A$ and $B$, your task is to merge these arrays into one sorted array, $C$. The elements in each of the arrays $A$ and $B$ are in non-decreasing order. The merged array $C$ should contain all the elements from $A$ and $B$ in non-decreasing order.

Try not to use any sort functions, or implement your own sort function.

## Input Format

- The first line contains an integer $N$, the size of array $A$.
- The second line contains $N$ space-separated integers, the elements of array $A$.
- The third line contains an integer $M$, the size of array $B$.
- The fourth line contains $M$ space-separated integers, the elements of array $B$.

## Output Format

Output one line containing the merged array $C$, with its elements separated by spaces.

## Sample
```input1
3
1 3 5
4
2 4 6 8
```

```output1
1 2 3 4 5 6 8
```

```input2
2
1 2
3
3 4 5
```

```output2
1 2 3 4 5
```

## Specification
- $1 \leq N, M \leq 10^5$
- $-10^9 \leq A_i, B_i \leq 10^9$ for all $1 \leq i \leq N$ for $A_i$ and $1 \leq i \leq M$ for $B_i$
- Arrays $A$ and $B$ are sorted in non-decreasing order.
