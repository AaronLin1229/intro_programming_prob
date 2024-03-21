## Problem Description
In a recent quiz competition, the scoring system is designed to reward participants based on the number of questions they answer correctly. The scoring is as follows:
- For $0$ to $10$ correct answers, each correct answer is worth $6$ points.
- For $11$ to $20$ correct answers, the first $10$ answers are worth $6$ points each, and each subsequent answer is worth $2$ points.
- For $21$ to $40$ correct answers, the first $20$ answers are calculated as above, and each subsequent answer is worth $1$ point.
- For more than $40$ correct answers, the participant scores a flat $100$ points regardless of the exact number.

Your task is to write a program that calculates the total score of a participant based on the number of correct answers they provide.

## Input Format
A single line containing an integer $s$ representing the number of correct answers.

## Output Format
Output a single integer, the total score of the participant.

## Sample

```input1
8
```

```output1
48
```

```input2
15
```

```output2
70
```

```input3
25
```

```output3
85
```

## Specification
- $1 \leq s \leq 100$
