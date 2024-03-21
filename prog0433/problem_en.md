## Problem Description

Given a sequence of nonzero integers, please print the number of consecutive integers with the same sign. If the consecutive integers are negative, print a minus sign before the number, i.e., make it a negative integer.

## Input Format

There is one line in the input, which is a sequence of nonzero integers separated by space. All inputs and all arithmetics are in int.

## Output Format

There is one line in the output, which is a sequence of the number of consecutive integers with the same sign separated by space.

## Sample

```input1
-1 -2 -3 4 5 -6
```

```output1
-3 2 -1
```

The first $3$ numbers $−1, −2, −3$ are negative but the fourth number $4$ is positive, so we print $−3$. Then, the next $2$ numbers $4, 5$ are positive but the sixth number $−6$ is negative, so we print $2$. Finally, the only last number $−6$ is negative, so we print $−1$.

## Source

Judge Girl