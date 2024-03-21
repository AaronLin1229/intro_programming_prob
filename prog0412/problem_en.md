## Problem Description

Given two positive integers, $a$ and $b$, calculate the greatest common divisor $\gcd(a, b)$ of the two numbers using the following definition:

$$
\gcd(a, b) =
\begin{cases}
a & \text{if } b = 0\\
\gcd(b, a \bmod b) & \text{otherwise}
\end{cases}
$$

Note that the $\gcd()$ operator satisfies the commutative property, meaning $\gcd(a, b) = \gcd(b, a)$.

## Input Format

Two positive integers $a$ and $b$, seperated by a space character.

## Output Format

A single integer representing the greatest common divisor of $a$ and $b$.

## Sample

```input1
12 15
```

```output1
3
```

```input2
101 10
```

```output2
1
```

## Specification
- $1 \leq a, b \leq 10^{8}$
