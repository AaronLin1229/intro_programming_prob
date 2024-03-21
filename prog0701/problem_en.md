## Problem Description

Write a problem to check if the inputted string is a valid Identity card number in Taiwan.

- A valid Identity card number should start with an upper case English letter, followed by 9 digits of number.

- The English letter should be replaced with a certain value using this table:

| Letter | Value |
|----|----|
| A  | 10 |
| B  | 11 |
| C  | 12 |
| D  | 13 |
| E  | 14 |
| F  | 15 |
| G  | 16 |
| H  | 17 |
| I  | 34 |
| J  | 18 |
| K  | 19 |
| L  | 20 |
| M  | 21 |
| N  | 22 |
| O  | 35 |
| P  | 23 |
| Q  | 24 |
| R  | 25 |
| S  | 26 |
| T  | 27 |
| U  | 28 |
| V  | 29 |
| W  | 32 |
| X  | 30 |
| Y  | 31 |
| Z  | 33 |

- The string after the letter getting replaced should be a string with 11 digits. For each digit from left to right, the value of the digit should be multiplied with $[1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]$, respectively. Afterwards, all values should be summed up to a single number $N$.

- If $N$ is a number divisible by $10$, then the Identity card number is valid, otherwise, it's invalid.


## Input Format

Input consists only one line, a string $s$ to be verified if it's a valid Identity card number.

## Output Format

Output `YES` if it is valid, `NO` otherwise.

## Sample

```input1
G236140903
```

```output1
YES
```

```input2
Q228821511
```

```output2
NO
```

## Hint

You are encouraged to write a function that takes in a string as input and returns the validness of the string.

## Specification

- $1 \leq |s| \leq 15$
- All characters in $s$ is either a Enslish letter or a digit.
