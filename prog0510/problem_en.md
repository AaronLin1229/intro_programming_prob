## Problem Description

Given a staircase with $N$ steps, calculate the number of distinct ways to reach the top. At each step, one can either climb 1 stair or 2 stairs. However, some stairs are broken and cannot be used.

## Input Format

- The first line contains an integer $N$, the number of stairs.
- The second line contains an integer $K$, the number of broken stairs.
- The third line contains $K$ space-separated integers $b_i$, each representing the position of a broken stair.

## Output Format

Output a single line containing the number of distinct ways to climb the staircase, avoiding the broken stairs.

## Sample

```input1
5
1
3
```

```output1
3
```

```input2
6
2
2 4
```

```output2
2
```

## Specification

- $1 \leq N \leq 40$
- $1 \leq K \leq N$
- $1 \leq b_i \leq N$

