## Problem Description

Given two positive integers, $a$ and $b$, calculate the least common multiple, $\text{lcm}(a, b)$, of the two numbers using the following equation:

$$
\text{lcm}(a, b) = \frac{ab}{\gcd(a, b)}
$$

Here, $\gcd(a, b)$ represents the greatest common divisor of $a$ and $b$.

## Input Format

Two positive integers $a$ and $b$.

## Output Format

A single integer representing the least common multiple of $a$ and $b$.

## Sample

```input1
4 6
```

```output1
12
```

```input2
21 6
```

```output2
42
```

## Specification
- $1 \leq a, b \leq 10^{6}$
