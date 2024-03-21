## Problem Description
An ant wants to go from position $A$ to position $B$, and two walls block the route. Both walls have $A$ thickness of one. Please find the square of the shortest distance from position $A$ to position $B$. Note that the wall width is the same as the road width, so the ant must climb over the walls to get to position $B$. Also, note that the distance between the two walls may be zero.

![img](file://p10318.png)

## Input Format
The input consists of 6 integers: $w, a, b, c, d, e$ Note that $w, a, c, d, e > 0$ and $b >= 0$.

All inputs and all arithmetics are in int.

## Output Format
The output is the square of the shortest distance from $A$ to $B$.

## Sample

```input1
5 3 4 3 2 6
```

```output1
809
```

```input2
5 6 0 7 5 6
```

```output2
754
```

## Specification
- $w, a, c, d, e > 0$
- $b >= 0$.
