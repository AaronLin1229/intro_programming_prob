## Problem Description

Recall prog0528. Game of Life, now you should write two functions about the $n \times n$ board of game of life:

1. `step(board, n)`: This function will simulate the game of one round.
2. `print(board, n)`: This fucntion will print the status of the board.

## Input Format

- The first line contains one integer $n$, the size of the board.
- The next $n$ lines each contain $n$ binary numbers, representing the initial configuration of the board. Here, 0 represents a dead cell and 1 a live cell.
- The last line contains an integer $m$, the number of rounds to simulate.

## Output Format

Output $n$ lines, each containing $n$ characters, representing the configuration of the board after $m$ rounds.e

## Sample

```input1
3
0 1 0
0 0 1
1 0 1
1
```

```output1
0 0 0
0 0 1
0 1 0
```

```input2
4
1 0 1 0
0 0 0 0
0 1 0 1
0 0 0 0
2
```

```output2
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
```

## Template

| C | C++ | Python |
| -------- | -------- | -------- |
| [main.c](file://main.c) | [main.cpp](file://main.cpp) | [main.py](file://main.py) |

## Specification

- $1 \leq n \leq 128$
- $0 \leq m \leq 100$
