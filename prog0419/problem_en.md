## Problem Description
Given two integers $h$ and $w$, your task is to create a rectangle with height $h$ and width $w$. The sides of the rectangle should be made with the dash `-` and pipe `|` characters for horizontal and vertical sides, respectively, and the corners should be represented by the character `O`.

## Input Format
A single line containing two space-separated integers $h$ and $w$.

## Output Format
Output $h$ lines representing the rectangle. The first and last characters of the first and last lines should be `O`, the characters between them should be `-`, the first and last characters of the intermediate lines should be `|`, and the characters between them should be spaces.

## Sample

```input1
3 5
```

```output1
O---O
|   |
O---O
```

```input2
4 4
```

```output2
O--O
|  |
|  |
O--O
```

## Specification
- $2 \leq h, w \leq 10$
