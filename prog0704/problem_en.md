## Problem Description

Implement a function `remove_leading_zeros(s)` that takes an input string representing a postive number, and removes the leading zeros. 

For a string that is is all zeros, you should make 1 zero remaining for the string.

For C, your string should modify it in-place, for C++ and Python, you should return the new string.

## Input Format

A string $s$.

## Output Format

String $s$ after removing the leading zeros.

## Sample

```input1
00001234
```

```output1
1234
```

```input2
00012321000
```

```output2
12321000
```

```input3
000000
```

```output3
0
```

## Template

| C | C++ | Python |
| -------- | -------- | -------- |
| [main.c](file://main.c) | [main.cpp](file://main.cpp) | [main.py](file://main.py) |

## Specification

- $1 \leq |s| \leq 1023$
- $s_i \in \{\text{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}\}$.
