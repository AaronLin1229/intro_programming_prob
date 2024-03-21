## Problem Description

Given a sequence of stock prices, you need to find out the longest length of given patterns. For simplicity we assume that two consecutive prices are different. There are two patterns to look for -- "valley" and "mountain". 

- A sequence $(a_1, \dots, a_i, \dots, a_n)$ is a valley if $(a_1, \dots, a_i)$ is decreasing and $(a_i, \dots, a_n)$ is increasing. 

- A sequence $(a_1, \dots, a_i, \dots, a_n)$ is a valley if $(a_1, \dots, a_i)$ is increasing and $(a_i, \dots, a_n)$ is decreasing. 

Your program will output the starting point and the length of the longest mountain or valley. If there are more than one sequence that have the longest length, choose the one with the longest left sequence. If the lengths of the left sequences are still the same, output the one that appears first.

Here is an example. If the sequence is $[6,5,4,5,4,3]$, it contains a valley $[6,5,4,5]$ and a mountain $[4,5,4,3]$. Both are $4$ in length. However, you need to choose $[6,5,4,5]$ because it has a longer left sequence length $3$.

If you cannot find any valley or mountain (the whole sequence is increasing or decreasing, or it contains nothing), you should output $0$.

## Input Format

The input is $x_1, x_2, \dots, x_n$, a sequence of integers, and you should process all of them until EOF. It is guaranteed that any two consecutive numbers are different.

## Output Format

Output the length of the longest valley or mountain and the index of the first element of that pattern. The index starts from $1$. If there are no valleys or mountains, output $0$.

## Sample

```input1
6 5 4 5 4 3
```

```output1
4 1
```

```input2
1 2 3 4 5 6 7 8 9
```

```output2
0
```

## Specification

- $0 \leq x_i \leq 20000, i = 1, 2, \dots, n$
- $0 \leq n \leq 40000$

## Source

Judge Girl