## Problem Description
Given two 3-dimensional vectors $\vec{V1} = (a, b, c)$ and $\vec{V2} = (d, e, f)$, your task is to calculate their inner product and cross product. The inner product should be outputted in the first line, and the cross product in the second line.

## Input Format
The first line contains three integers $a$, $b$, and $c$ representing the components of the first vector $\vec{V1}$.
The second line contains three integers $d$, $e$, and $f$ representing the components of the second vector $\vec{V2}$.

## Output Format
The first line should contain a single integer representing the inner product of $\vec{V1}$ and $\vec{V2}$.
The second line should contain three space-separated integers formatted as "x y z", representing the components of the cross product of $\vec{V1}$ and $\vec{V2}$.

## Sample

```input1
1 2 3
4 5 6
```

```output1
32
-3 6 -3
```

```input2
-1 0 3
4 5 -2
```

```output2
-10
-15 -10 5
```

## Specification
- $-100 \leq a, b, c, d, e, f \leq 100$
