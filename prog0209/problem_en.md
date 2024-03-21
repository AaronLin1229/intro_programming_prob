## Problem Description

We have four points $A$, $B$, $C$, and $D$ on the plane. These four points define a polygon as in the following figure. Note that all segments in the simple polygon are vertical or horizontal.

![img](file://sample.png)

Now write a program to calculate perimeter and area of the polygon defined by the four points $A$, $B$, $C$, and $D$. For example, the perimeter and the area of the figure above should be 20 and 16 respectively. Note that to make the perimeter and area well-defined we assume that point $D$ does not appear in the right bottom corner of point $B$. In other words, if the coordinates of point $B$ is $(B_x,B_y)$ and the coordinates of point $D$ is $(D_x,D_y)$, then $D_x$ is smaller than $B_x$ or $D_y$ is greater than $B_y$.

## Input Format

The input has eight lines for the x and y coordinates of points $A$, $B$, $C$, and $D$. The coordinates are all between $-10000$ and $10000$.

## Output Format

The output has two lines for the perimeter and the area of the simple polygon.

## Sample

```input1
0
0
2
2
4
6
2
4
```

```output1
20
16
```

## Specification

- $-10000 \lt x, y \lt 10000, \text{for all points}$

## Source

Judge Girl
