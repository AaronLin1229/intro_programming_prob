## Problem Description

Given a list of $N$ strings, your task is to sort them in non-descending order. Each string consists of characters with no spaces. The sorting should be done based on the lexicographical order (dictionary order).

## Input Format

The first line contains an integer $N$, the number of strings.
Each of the next $N$ lines contains a string.

## Output Format

Output $N$ lines, each containing one string, representing the sorted order of the given strings.

## Sample

```input1
3
cat
apple
banana
```

```output1
apple
banana
cat
```

## Specification

- $1 \leq N \leq 1000$
- Length of each string is at least $1$ and at most $31$.
- Each string consists of lowercase English letters only.
