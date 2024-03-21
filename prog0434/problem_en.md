## Problem Description

Given $N$ rectangles $R_1, R_2, \dots, R_N$, calculate the total area covered by these rectangles.

Each rectangle, denoted as $R_i$, is defined by the coordinates $(x_i,y_i)$ of its bottom-left corner, its width $w_i$, and its height $h_i$. The rectangles may overlap. Any two consecutive rectangles, $R_i$ and $R_{i + 1}$, must satisfy the following two constraints:

1. The bottom-left corner of $R{i+1}$, denoted as $(x_{i+1},y_{i+1})$, must lie inside the boundaries of $R_i$. In other words, $x_i < x_{i + 1} < x_i + w_i$ and $y_i < y_{i + 1} < y_i + h_i$.

2. The top-right corner of $R_{i+1}$ must lie outside the boundaries of $R_i$, meaning it must be above and to the right of the top-right corner of $R_i$.

![img](file://sample.png)

Write a program that accepts the descriptions of these rectangles as input and calculates the total area covered by them.

Note that you cannot use an array to store the inputs, as it may lead to an out-of-memory situation.

## Input Format

- The first line contains one integer $N$, which is the number of rectangle and $N \geq 2$.
- Next $N$ line contains four integers: $x, y, w, h$ ($w, h \gt 0$), representing the coordinates of the bttom-left corner, width, and height of each rectangle.

## Output Format

A single integer, the total area covered by the given rectangles.

## Sample

```input1
3 
0 0 3 4 
1 2 3 3 
3 3 4 4
```

```output1
31
```

## Source

Judge Girl