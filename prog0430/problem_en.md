## Problem Description

We have many positive integers, and we want to find the maximum length of the connected integer sequence. Two integers are connected if the LSD (Least Significant Digit) of the previous number is as same as the MSB (Most Significant Digit) of the current number.

For example, if we have three integers “1234”, “432”, and “12” as a sequence.

[!img](file://sample.png)

The maximum length of the connected integer sequence is $7$, which is the sum of the length of “1234” and “432”. Note that "432" is NOT connected to "12" since 2 from "432" is not the same as the 1 from "12". Also note that the maximum length sequence could be anywhere within the sequence of numbers, not necessarily from the beginning.

## Input Format

The input has one line of positive integers. There is a least one number in the input and you must process all of them until EOF.

## Output Format

The output is the maximum length of connected integer sequence.

## Sample

```input1
123
```

```output1
3
```

```input2
19 84 654 2145012300 1
```

```output2
10
```

```input3
1 12 234 5 6789 9101112
```

```output3
11
```

## Hint

You can get the most significant digit and the number of digits of a number by repeatedly dividing it by $10$, until it is less than $10$. For example if the number is "362", then you get 36, then you get 3, which is less than $10$. You get to this by two steps, so the number of digits is $3$.

## Specification

- All numbers are greater than 0 and are in `int`

## Source

Judge Girl