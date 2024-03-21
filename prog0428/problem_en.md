## Problem Description

Write a program to find the alternating sequence from the input that has the maximum length. A $k$-alternating sequence is a sequence of alternating $k$ positive integers and $k$ negative integers that starts and ends both with $k$ positive integers, and contains **at least one** set of $k$ negative integers in between. For example, when $k$ is $2$ then $(2, 1, −3, −2, 7, 100)$ is a $2$-alternating sequence, but none of $(1, 1, −23, 4)$, $(1, 2)$, $(1, 1, 3, −1, 1, 1)$ is.

Let us consider the following example. Now given an input sequence $(−3, 4, 6, −5, −3, 10, 7, −1, −1, 3, −7, 3)$, then $(4, 6, −5, −3, 10, 7)$ is the longest $2$-alternating sequence and $(3, −7, 3)$ is the longest $1$-alternating sequence.

Now given $k$ and a sequence of $n$ integers that ends in $0$, please find the length of the longest $k$-alternating sequence. If there are no $k$-alternating sequences in the input please report $0$.

## Input Format

There are two lines in the input. The first line has the integer $k$. The second line has the sequence integers end with $0$.

## Output Format

Only one line print the length of the longest $k$-alternating sequence.

## Sample

```input1
1
1 -1 1 1 -1 1 -1 1 0
```

```output1
5
```

```input2
2
-3 4 6 -5 -3 10 7 -1 -1 3 -7 3 0
```

```output2
6
```

## Explain for Sample 1

```
k = 1
(1 -1 1) 1 -1 1 -1 1 0
length = 3
1 -1 1 (1 -1 1 -1 1) 0
length = 5
```

## Explain for Sample 2

```
k = 2
-3 (4 6 -5 -3 10 7) -1 -1 3 -7 3 0
length = 6
```

## Hint

We observe that since the sequence ends in $0$, there will be only segments of positive and negative numbers before that. Therefore you only need to remember whether you are in the middle of a positive or negative segment, and how many numbers you have seen in this segment. Also you need to remember whether you are in the middle of an alternating sequence or not. Now whenever you switch from a positive segment to a negative segment, or from a negative to a positive segment, you need to update these information, and the length of the longest sequence you have seen so far. After processing through the sequence you will know the answer.

## Specification

- 30 pt: $1 \leq n \leq 20, k = 1$
- 60 pt: $1 \leq n \leq 100000, 1 \leq k \leq n$
- 10 pt: $n \geq 0, 1 \leq k \leq n$

## Source

Judge Girl