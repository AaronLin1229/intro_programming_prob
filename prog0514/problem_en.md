## Problem Description

Given an array $A$ of $N$ integers, your task is to check if the array is sorted in non-decreasing order. Print `YES` if it is sorted, otherwise print `NO`.

If an array $A$ is sorted in non-decreasing order, then it is equvilant to say that:

$$
A_i \leq A_j, \forall i \lt j
$$

## Input Format

The first line contains an integer $N$, the size of the array.
The second line contains $N$ integers separated by spaces, representing the elements of the array $A$.

## Output Format

Print `YES` if the array is sorted in non-decreasing order, otherwise print `NO`.

## Sample

```input1
3
1 2 3
```

```output1
YES
```

```input2
3
3 2 1
```

```output2
NO
```

```input3
3
1 1 1
```

```output3
YES
```

## Specification
- $1 \leq N \leq 10^5$
- $-10^9 \leq A_i \leq 10^9$ for $1 \leq i \leq N$
