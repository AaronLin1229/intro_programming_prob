## Problem Description

We have a two-dimensional $N \times N$ array. Each element of the array is either $0$ or $1$. Write a program to compute the length of the longest consecutive $1$'s in a row, in a column, or in a diagonal direction. You only need to consider the diagonal direction as going from $(x,y)$ to $(x+1,y+1)$, as in the following figure.

![img](file://1.jpeg)

The following figure has three examples.

![img](file://2.jpeg)


## Input Format

- The first line has the integer $N$, the size of the array. 
- The next $N$ lines have $N$ integers, which are either $0$ or $1$. They are the elements of the array.

$0 < N < 1000$ 

## Output Format

The output has only one integer -- the length of the longest consecutive $1$'s in a row, in a column, or in the diagonal direction.

## Sample

```input1
5
1 0 1 1 0
1 0 0 0 1
0 1 1 1 1
0 1 0 0 1
0 0 0 1 0
```

```output1
4
```

```input2
5
1 0 1 1 0
1 0 0 0 1
1 0 1 1 0
0 1 0 0 1
0 0 0 0 1
```

```output2
3
```

```input3
5
0 0 1 1 0
0 0 0 0 1
1 1 0 1 0
0 1 1 0 1
0 0 0 1 1
```

```output3
3
```

## Source

Judge Girl