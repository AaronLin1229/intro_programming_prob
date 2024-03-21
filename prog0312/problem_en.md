## Problem Description
Given a quadratic equation of the form $a x^2 + b x + c = 0$, where $a$, $b$, and $c$ are integers, determine the number of distinct real solutions for $x$, and if any, output the solutions in ascending order.

## Input Format
A single line containing three integers, $a$, $b$, and $c$, separated by a space.

## Output Format
The first line should contain a single integer indicating the number of distinct real solutions to the equation. If there are solutions, the second line should list the solutions as floats in ascending order, separated by a space.

## Sample

```input1
1 -3 2
```

```output1
2
1.0 2.0
```

```input2
1 4 4
```

```output2
1
-2.0
```

## Specification
- $1 \leq a, b, c \leq 10^{6}$
