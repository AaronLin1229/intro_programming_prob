Write a program to simulate a tank movement on a map.

## Problem Description

We have an $N$ by $N$ map with an $L$ by $W$ tank and $O$ obstacles. The vertical index is from $0$ to $N − 1$ , and the horizontal index is from $0$ to $M − 1$. An integer in every cell of the map indicates the status of the cell. A $0$ is a space, a $1$ is a tank, and a $2$ is an obstacle. Note that we will use the upper left corner of the tank to indicate its position, and the initial position of the tank is $(0,0)$. The tank will move according to instructions. Each instruction is a number from $0$ to $5$, indicating the direction the tank should go or we should print the map. Let the current position of the upper left corner of the tank be $(x,y)$.

- If the instruction is $0$, output the current map information.
- If the instruction is $1$, the tank moves from $(x,y)$ to $(x+1,y)$.
- If the instruction is $2$, the tank moves from $(x,y)$ to $(x,y+1)$.
- If the instruction is $3$, the tank moves from $(x,y)$ to $(x−1,y)$.
- If the instruction is $4$, the tank moves from $(x,y)$ to $(x,y−1)$.
- If the instruction is $5$, the tank moves from $(x,y)$ to $(x+1,y+1)$.

The coordinate system is defined as follows:

![img](file://1.png)

Note that if an instruction moves the tank out of the map or hit more than one obstacle, the tank will not move. Otherwise, the tank will move in the intended direction.

Write a program to simulate a tank movement on the map and output the map information if the instruction is $0$. The program moves the tank, initially located at $(0,0)$, according to the input instructions until the end of the file. There is at least one instruction, and the initial area of the tank has no obstacles.

Take sample input 3, for example, in the figure below.

![img](file://2.png)

## Input Format

The input contains only one test case. The first line contains four integers, $N, M, L, W$ representing the length and width of the map and the tank. The second line contains one integer $O$ representing the number of obstacles. For the following $O$ lines, each line contains two integers, representing the $x, y$ coordinate of obstacles.The last line contains the instructions for the tank, and the number of instructions is at least one.

## Output Format

Print the current map information if the instruction is 0.

## Sample

```input1
5 5 1 1
4
2 1
2 3
4 1
4 4
2 1 4 3 1 2 2 2 2 1 1 1 0
```

```output1
00000
00202
00000
00200
00001
```

```input2
4 5 2 3
6
0 2
1 2
1 3
2 3
3 0
4 2
0 2 0 1 3 2 0
```

```output2
11120
11100
22002
02200
11120
11100
22002
02200
11100
11100
22002
02200
```

```input3
4 5 2 3
6
0 2
1 2
1 3
2 3
3 0
4 2
0 5 4 0 5 1 3 2 0
```

```output3
11120
11100
22002
02200
01110
01110
20002
02200
00000
01110
21110
02200
```

## Specification

- $0 \lt N, M, L, W \lt 500$
- $0 \leq O \lt N \times M − L \times W$

## Source

Judge Girl