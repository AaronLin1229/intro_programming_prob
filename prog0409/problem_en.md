## Problem Description
Write a program to count the number of integers that are in the form of $3k$, $3k+1$, and $3k+2$ respectively, where $k \in \mathbb{N}$. For each integer, determine which form it belongs to and count the total number of integers for each form.

## Input Format
The first line contains a single integer $n$ (the number of input integers). Each of the following $n$ lines contains an input integer.

## Output Format
Output three numbers in a line. The first number is the count of integers in the form of $3k$, the second number is for $3k+1$, and the third number is for $3k+2$.

## Sample

```input1
5
1
2
3
4
5
```

```output1
1 2 2
```

```input2
10
3
1
4
1
5
9
2
6
5
3
```

```output2
4 3 3
```

## Specification
- $1 \leq n \leq 20$
- Each integer will be between $0$ and $10^9$.
