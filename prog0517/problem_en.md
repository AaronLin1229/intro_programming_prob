## Problem Description

Given a sorted array $A$ of $n$ integers, remove the duplicates in-place such that each element appears only once and return the new length $m$. 

## Input Format

The first line contains an integer $n$, the number of elements in the array.
The second line contains $n$ integers describing the elements of array $A$.

## Output Format

The first line should contain an integer $m$, the length of the array after duplicates have been removed.
The second line should contain $m$ integers, the elements of array $B$ after removing duplicates from array $A$.

## Sample

```input1
5
1 1 2 2 3
```

```output1
3
1 2 3
```

```input2
4
2 2 2 2
```

```output2
1
2
```

## Specification

- $1 \leq n \leq 10^5$
- $0 \leq A_i \leq 10^9, \text{for} 1 \leq i \leq n$
- Array $A$ is sorted in non-decreasing order.

## Source

Leetcode