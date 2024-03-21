## Problem Description

Little Bob likes playing with his box of bricks. He puts the bricks one upon another and builds stacks of different height. “Look, I’ve built a wall!”, he tells his older sister Alice. “Nah, you should make all stacks the same height. Then you would have a real wall.”, she retorts. After a little consideration, Bob sees that she is right. So he sets out to rearrange the bricks, one by one, such that all stacks are the same height afterwards. But since Bob is lazy he wants to do this with the minimum number of bricks moved. Can you help?

![img](file://sample.gif)

## Input Format

The input consists of several data sets. Each set begins with a line containing the number $n$ of stacks Bob has built. The next line contains $n$ numbers, the heights $h_i$ of the $n$ stacks. The total number of bricks will be divisible by the number of stacks. Thus, it is always possible to rearrange the bricks such that all stacks have the same height. The input is terminated by a set starting with $n = 0$. This set should not be processed.

## Output Format

For each set, first print the number of the set, as shown in the sample output. Then print the line `The minimum number of moves is k.`, where $k$ is the minimum number of bricks that have to be moved in order to make all the stacks the same height. Output a blank line after each set.

## Sample

```input1
6
5 2 4 1 7 5
3
1 1 1
0
```

```output1
Set #1
The minimum number of moves is 5.

Set #2
The minimum number of moves is 0.

```

## Specification

- $1 \leq n \leq 50$
- $1 \leq h_i \leq 100$

## Source

UVa Judge