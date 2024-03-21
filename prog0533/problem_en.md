## Problem Description

Given a Minesweeper field, write a program to replace all the blank cells with the number of mines adjacent to them (including diagonally adjacent mines). Mines are represented by `*` and blank cells by `.`.

## Input Format

The first line contains two integers $N$ and $M$, representing the number of rows and columns of the Minesweeper field, respectively.
The next $N$ lines each contain a string of $M$ characters, representing the Minesweeper field.

## Output Format

Output $N$ lines, each containing a string of $M$ characters, representing the Minesweeper field with all blank cells replaced by the number of adjacent mines.

## Sample

```input1
4 4
*...
....
.*..
....
```

```output1
*100
2210
1*10
1110
```


## Specification
- $1 \leq N, M \leq 100$
- Each line of the Minesweeper field contains only `*` and `.` characters.
