## Problem Description

The [Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life), also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970. The game is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves.

The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, alive or dead. Every cell interacts with its eight neighbors, which are the cells that are horizontally, vertically, or diagonally adjacent.

At each step in time, the following transitions occur:
1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The initial pattern constitutes the 'seed' of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed—births and deaths occur simultaneously.

In this problem, you are given an initial configuration for the Game of Life. Your task is to simulate the game for $k$ rounds and output the final configuration.

## Input Format

- The first line contains two integers $n$ and $m$, the dimensions of the grid.
- The next $n$ lines each contain $m$ binary numbers, representing the initial configuration of the grid. Here, 0 represents a dead cell and 1 a live cell.
- The last line contains an integer $k$, the number of rounds to simulate.

## Output Format

Output $n$ lines, each containing $m$ characters, representing the configuration of the grid after $k$ rounds.

## Sample

```input1
3 3
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
4 4
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

## Specification

- $1 \leq n, m \leq 100$
- $0 \leq k \leq 100$
