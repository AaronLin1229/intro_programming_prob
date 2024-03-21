## Problem Description

In this problem, you are given an array of integers $A$ of length $N$. Your task is to find the maximum subarray sum in $A$.

A subarray is defined as a contiguous part of the array and must contain at least one element. For instance, if the array is $[1, -3, 2, 1, -1]$, some of the subarrays are $[1]$, $[1, -3]$, $[-3, 2, 1]$, etc.

## Input Format

- The first line contains an integer $N$, the size of the array.
- The second line contains $N$ space-separated integers, representing the elements of the array $A$.

## Output Format

Print a single integer, the maximum sum of any subarray of $A$.

## Sample

```input1
5
1 -3 2 1 -1
```

```output1
3
```

```input2
3
-1 -2 -3
```

```output2
-1
```

## Specification

- $1 \leq N \leq 10^3$
- $-10^5 \leq A_i \leq 10^5$ for each $1 \leq i \leq N$
