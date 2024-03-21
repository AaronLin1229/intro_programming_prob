## Problem Description

Write a program to simulate Origami. The paper is an $r$ by $c$ matrix, and your program needs to fold it. After folding, we add the two numbers falling in the same position together and reduce the size of the paper accordingly. There are three types of folding. The first is to fold down the matrix by $k$ rows. For example, if $k$ is $2$, you need to add the first row to the fourth row, add the second row to the third row on the top, and reduce the number of rows by $2$. Please refer to the following figure.

![img](file://1.png)

The second is to fold to the left of the matrix by $k$ columns. For example, if $k$ is $3$, you need to add the rightmost column to the sixth row to the right, add the second column to the fifth column to the right, add the third column to the fourth column to the right and reduce the number of the columns by $3$. Please refer to the following figure.

![img](file://2.png)

The third is to fold the top right corner diagonally. We keep the diagonal elements the same and add each element in the upper triangular part to its corresponding element in the lower triangular part. Then we set all elements in the upper triangular to $0$. The numbers of rows and columns remain the same. Please refer to the following figure.

![img](file://3.png)

## Input Format

- The first input line has $r$ and $c$; both are no more than $600$.
- Each of the following $r$ lines has $c$ integers in the matrix.
- Each of the remaining lines has two integers for folding, and you need to process all of them until EOF. The first integer is the type of folding. $1$ folds down, $2$ folds left, and $3$ folds diagonally. The second integer represents the folding size $k$.
- All folding will not go beyond the lower-left corner.
- The $k$ in diagonal folding will be larger than $1$.
- No integer arithmetic will cause overflow.

## Output Format

You need to print the matrix after folding. Each line represents a row in the remaining matrix.

## Sample

```input1
8 3
1 2 3
6 5 4
6 5 4
2 4 6
0 1 2
1 2 3
4 5 6
7 8 9
1 2
```

```output1
12 10 8
3 6 9
0 1 2
1 2 3
4 5 6
7 8 9
```

```input2
5 9
0 9 0 9 6 9 7 3 1
1 8 1 8 5 8 4 4 2
2 7 2 7 4 6 3 5 4
3 6 3 6 3 4 1 7 5
4 5 4 5 2 2 2 8 3
2 3
```

```output2
0 9 0 10 9 16
1 8 1 10 9 12
2 7 2 11 9 9
3 6 3 11 10 5
4 5 4 8 10 4
```

```input3
8 6
0 8 21 9 5 3
1 7 9 17 8 1
2 6 8 3 12 6
3 2 4 3 3 15
4 1 1 7 2 9
5 3 2 9 3 4
6 0 5 4 5 5
7 1 6 6 4 6
3 4
```

```output3
0 8 21 0 0 0
1 7 18 17 0 0
2 6 13 11 12 0
3 2 7 4 9 15
4 1 1 7 2 9
5 3 2 9 3 4
6 0 5 4 5 5
7 1 6 6 4 6
```

```input4
6 5
1 2 4 5 1 
0 0 2 4 5 
5 4 4 3 0 
3 0 5 3 4 
2 4 1 5 0 
3 1 5 3 4 
3 2
1 3
2 2
```

```output4
8 8 15 
2 9 13 
4 7 17
```

## Source

Judge Girl