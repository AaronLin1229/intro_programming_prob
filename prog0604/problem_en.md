## Problem Description

Write a function in C/C++ or Python to count the positive and negative numbers in a given array.

The C/C++ function should be

```cpp
void count_pos_neg(int arr[], int n, int res[2])
``` 

where `arr[]` is the array we want to count for positive and negative numbers, `n` is the size of `arr[]`. And we want to store the results in `res`, where `res[0]` stroes the count for positive numbers, and `res[1]` stroes the count for negative numbers.

The Python function should be 

```Python
def count_pos_neg(arr: list[int]) -> list[int]
```

where `arr` is the array we want to count for positive and negative numbers. We would return the count of the positive and negative numbers in a list of size 2, where the first element is the count of positive numbers, and the second element is the count of negative numbers.


## Input Format

The first line contains a single integer $n$ (the size of the array).
The second line contains $n$ integers separated by space, representing the elements of the array $A$.

## Output Format

Output two integers separated by space. The first integer is the count of positive numbers, and the second integer is the count of negative numbers in the array.

## Sample

```input1
5
-1 2 3 -4 5
```

```output1
3 2
```

```input2
4
-3 -2 -1 0
```

```output2
0 3
```

## Template

| C | C++ | Python |
| -------- | -------- | -------- |
| [main.c](file://main.c) | [main.cpp](file://main.cpp) | [main.py](file://main.py) |

## Specification
- $1 \leq n \leq 10^4$
- $-10^9 \leq A_i \leq 10^9$, where $1 \leq i \leq n$
