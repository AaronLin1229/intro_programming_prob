## Problem Description

Write a program to compute the maximum number of consecutive $\text{1}$'s in the binary representation of a set of positive integers. For instance, the integer $7$ has three consecutive $\text{1}$'s as its binary representation is $\text{00000111}$. Similarly, the integer $25$ has two consecutive $\text{1}$'s because its binary representation is $\text{00011001}$.

## Input Format

The input will be a set of positive integers, each not exceeding $2147483647$, given one per line. Your program should continue processing until EOF (End Of File).

## Output Format

For each integer in the input, output the maximum number of consecutive $\text{1}$'s found in its binary representation. Each output should be on a new line.

## Sample

```input1
1
126
25
7
65535
21
2147483647
```

```output1
1
6
2
3
16
1
31
```

## Specification

- Each input integer will be in the range $[1, 2147483647]$.

## Source

Judge Girl