## Problem Description
Given a temperature in Fahrenheit, your task is to convert it into Celsius. The input will be a double float representing the Fahrenheit temperature, and the output should be the corresponding Celsius temperature, also as a double float.
The formula for converting Fahrenheit to Celsius is:

$$
C = (F - 32) \times \frac{5}{9}
$$

## Input Format
A single line containing a double float $F$, the temperature in Fahrenheit.

## Output Format
A single line containing a double float, the temperature in Celsius converted from the given Fahrenheit temperature. The answer would be accpected if the difference between the submitted output and the answer is less than $10^{-6}$.

## Sample

```input1
212
```

```output1
100
```

```input2
32
```

```output2
0
```

## Specification
- $-10^3 \leq F \leq 10^3$

