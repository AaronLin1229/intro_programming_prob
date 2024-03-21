## Problem Description

You are given an array of positive integers, $A$, which can be imagined as a seesaw. The task is to determine if there exists an index in $A$ where a pivot can be placed such that the seesaw is balanced. The seesaw is balanced if the sum of the weights (integer values) on either side of the pivot is equal. If such an index exists, print the index (1-indexed). If no such index exists, print `NO`.

Let us consider an example. Let $N$ be $5$ and the numbers are $[2, 1, 5, 3, 1]$. If we place the pivot on the third position. The seesaw would balance since $3 \times 2 + 1 \times 1 = 3 \times 1 + 2 \times 2$.

![img](file://sample.png)

## Input Format

The first line contains a single integer $N$, the size of the array $A$.
The second line contains $N$ space-separated integers, the elements of the array $A$.

## Output Format

Print a single line containing either the 1-indexed position of the pivot that balances the seesaw or `NO` if no such pivot exists.

## Sample

```input1
5
2 1 5 3 1
```

```output1
3
```

```input2
4
1 2 3 4
```

```output2
3
```

```input3
8
3 1 4 1 5 9 2 6
```

```output3
NO
```

## Specification
- $1 \leq N \leq 20000$
- $1 \leq A_i \leq 10000, 1 \leq i \leq N$.
