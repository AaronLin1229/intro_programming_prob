## Problem Description
Write a program that takes a single integer $P$ representing a percentage grade as input and outputs the corresponding letter grade based on the grading scale provided.

| Letter Grade | GPA Value | Percentage Range |
|--------------|-----------|------------------|
| A+           | 4.3       | 90–100           |
| A            | 4.0       | 85–89            |
| A−           | 3.7       | 80–84            |
| B+           | 3.3       | 77–79            |
| B            | 3.0       | 73–76            |
| B−           | 2.7       | 70–72            |
| C+           | 2.3       | 67–69            |
| C            | 2.0       | 63–66            |
| C−           | 1.7       | 60–62            |
| F            | 0         | 59 and below     |

## Input Format
A single integer, $P$, where $0 \leq P \leq 100$.

## Output Format
A single string, the letter grade that corresponds to the percentage $P$.

## Sample

```input1
95
```

```output1
A+
```

```input2
88
```

```output2
A
```

## Specification
- $0 \leq P \leq 100$