## Problem Description

Given an array $A$ of $n$ integers, find two numbers such that they add up to a specific target number $k$. Your task is to identify the indices of these two numbers in the array. The array indices start from 1. It is guaranteed that there is exactly one solution, and you may not use the same element twice.

## Input Format

- The first line contains an integer $n$, the size of the array $A$.
- The second line contains $n$ integers, representing the elements of the array $A$.
- The third line contains the target number $k$.

## Output Format

Print two space-separated integers, the indices of the two numbers whose sum equals $k$. The smaller index should be printed first.

## Sample

```input1
4
2 7 11 15
9
```

```output1
1 2
```

```input2
3
3 2 4
6
```

```output2
2 3
```

## Specification

- $2 \leq n \leq 10^3$
- $-10^9 \leq A_i \leq 10^9$
- $-10^9 \leq k \leq 10^9$
- There is exactly one solution.

## Source

Leetcode