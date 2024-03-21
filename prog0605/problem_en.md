## Problem Description

In this problem, you are required to calculate the binomial coefficient $C^n_k$, which is the number of ways to choose $k$ elements out of a set of $n$ elements without regard to the order of selection. The binomial coefficient is defined as:

$$
C^n_k = \frac{n!}{k!(n-k)!}
$$

where $n!$ denotes the factorial of $n$.


## Input Format

The input contains two integers, $n$ and $k$, separated by a space.

## Output Format

Output a single integer, the value of $C^n_k$.

## Sample

```input1
5 2
```

```output1
10
```

```input2
6 3
```

```output2
20
```

## Template

| C | C++ | Python |
| -------- | -------- | -------- |
| [main.c](file://main.c) | [main.cpp](file://main.cpp) | [main.py](file://main.py) |

## Specification

- $n$: Integer in the range $[0, 12]$
- $k$: Integer in the range $[0, n]$
