## Problem Description

Given $N$ license plates, output the valid license plates in ASCII order.

There are two kinds of license plates. The first kind has the form $x_1x_2-x_3x_4x_5x_6$ and the second kind has the form $x_1x_2x_3-x_4x_5x_6$, where $x_1$ to $x_6$ are non-space characters.

A license plate is valid if it satisfies all the following constraints:
- $x_1$ to $x_6$ are all alphabets or digits.
- $x_1$ to $x_6$ should contain at least one digit, and the sum of all the digits cannot be divided by 7.
- $x_1$ to $x_6$ should not contain the same character (both digits and alphabets) more than twice. The alphabets are case sensitive.
- $x_1$ to $x_6$ should not contain two or more consecutive digit 4. For example, "ab-44cd" is invalid. Note that $x_2$ and $x_3$ are not consecutive in the first kind of the license plate, and $x_3$ and $x_4$ are not consecutive in the second kind of the license plate.

Output the first kind of valid license plates in ASCII order, i.e., '0' < '1' < ... < '9' < 'A' < ... < 'Z' < 'a' < …< 'z'. Then, output the second kind of valid license plates in ASCII order.

## Input Format

Input contains one test case. The first line is an integer $N$, indicating the number of the license plates. For the following $N$ lines, each line contains a string with exactly $7$ non-space characters.

## Output Format

Output the valid license plates. Output the first kind of the valid license plates in ASCII order. Then output the second kind of the valid license plates in ASCII order.

## Sample

```input1
13
9XP-DDE
9XP-DDe
oL-H8GE
48-u#ck
Gg-j7dJ
zxY-RAp
2zK-jjj
abcdefg
x-A869w
YG1-37p
QI-8EpK
PU-P+1g
f2a-E4Z
```

```output1
QI-8EpK
oL-H8GE
9XP-DDE
9XP-DDe
YG1-37p
f2a-E4Z
```

## Specification

- $1 \leq N \leq 30$

## Source

Judge Girl