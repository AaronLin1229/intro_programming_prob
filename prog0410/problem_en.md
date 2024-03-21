## Problem Description
Given the oriented coordinates of a polygon $P = \{(x_i, y_i) : i = 1, ..., n\}$, please calculate twice the area of the polygon, denoted as $2A$. Here oriented means that the coordinates are given counterclockwise from the first vertex to the last vertex. Note that you should not use an array to store the coordinates in this problem because the number of vertices is large.

Hint: You can use the Shoelace formula to calculate twice the area of the polygon:

$$
2A = \begin{vmatrix}x_1 & x_2\\ y_1 & y_2\end{vmatrix} + \begin{vmatrix}x_2 & x_3\\ y_2 & y_3\end{vmatrix} + \cdots + \begin{vmatrix}x_n & x_1\\ y_n & y_1\end{vmatrix}
$$

For example, given $P = \{(5, 5), (2, 5), (5, 1)\}$

![img](file://10363.png)

We can calculate twice the area of $P$ by:

$$
2A = \begin{vmatrix}5 & 2\\ 5 & 5\end{vmatrix} + \begin{vmatrix}2 & 5\\ 5 & 1\end{vmatrix} + \begin{vmatrix}5 & 5\\ 1 & 5\end{vmatrix} = 15 - 23 + 20 = 12
$$


## Input Format
- The first line contains one number $n$, where $n$ denotes the number of vertices.
- Each of the following $n$ lines has two number $x_i$ and $y_i$.

## Output Format
The output contains a single number, which represents twice the area of the polygon.

## Sample

```input1
3
5 5
2 5
5 1
```

```output1
12
```

## Specification
- All inputs and arithmetic are in int.
- No integer arithmetic will cause overflow.

## Source
Judge Girl