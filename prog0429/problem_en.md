## Problem Description

You will be given a sequence of blocks. Each block starts with an $N$ that indicates the number of integers in the block, then follows with a sequence of $N$ integers. Write a program to read the sequence of blocks until the end of file, and print the maximum or the minimum in each block according to the following rules. Note that to make the maximum and minimum well-defined we assume that every block has at least one number. Also we assume that there is at least one block.

- A block is complete if it has $N$ numbers. In this case report the maximum of the numbers with this block.
- A block is incomplete if it is the last block and the number of integer is less than $N$. In this case report the minimum of the numbers in this block.

Let us illustrate the task with two examples:

If we are given $[3, -14, 36, 7], [2, 79, 24], [2, 15, 9]$, then we should print $36, 79, 15$ since every block is complete and we need to print the maximum. If we are given $[4, 34, 17, 0, 97], [1, 37], [2, 1, -12], [5, 13, -5, 63]$ then we need to print $97, 37, 1, -5$ because the last block is incomplete, and we need to print the minimum. Note again that only the last block could be incomplete.

Do not use array for this problem. You can solve this problem with very little memory. We will make sure that you will not have enough memory, and see the "memory limit exceeded" error, if you use array.

## Input Format

The input contains only one test case. Each test case contains a sequence of integers. $N$ is a positive integer.

## Output Format

Print all integers on separate lines.

## Sample

```input1
3 -14 36 7 2 79 24 2 15 9
```

```output1
36
79
15
```

```input2
4 34 17 0 97 1 37 2 1 -12 5 13 -5 63
```

```output2
97
37
1
-5
```

## Specification

- $N$ is a positive integer.
- $10000 \leq \text{ Each integer in a block } \leq 10000$

## Source

Judge Girl