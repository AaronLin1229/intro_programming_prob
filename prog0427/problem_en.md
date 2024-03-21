## Problem Description

Write a program that continuously reads integers from the input. For each integer read, the program should output two numbers: the current maximum number encountered so far and the count of how many times this maximum number has appeared.

Note that you should avoid the use of array since the input size could be big.

## Input Format

The input consists of several lines, each containing a single integer. The input is terminated by the end-of-file (EOF) marker.

## Output Format

For each integer read from the input, output a line containing two integers separated by a space. The first integer is the maximum number encountered up to that point, and the second integer is the count of how many times this maximum number has appeared in the input so far.

## Sample

```input1
1
2
3
4
5
```

```output1
1 1
2 1
3 1
4 1
5 1
```

```input2
5
4
3
2
1
```

```output2
5 1
5 1
5 1
5 1
5 1
```

```input3
3
3
3
4
4
4
5
5
5
```

```output3
3 1
3 2
3 3
4 1
4 2
4 3
5 1
5 2
5 3
```

```input4
5
5
5
4
3
4
5
5
5
```

```output4
5 1
5 2
5 3
5 3
5 3
5 3
5 4
5 5
5 6
```

## Specification

- $1 \leq \text{each number} \leq 100$