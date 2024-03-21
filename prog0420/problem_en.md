## Problem Description
Given two integers $h$ and $w$, your task is to create a rectangle with height $h$ and width $w$, consisting of `+` and `-`. The top-left cornor of the rectangle should be a `+`. For every `+` in the rectangle, its four sides should be `-`, and for every `-` in the rectangle, its four sides should be `+`, except for the broader.

## Input Format
A single line containing two space-separated integers $h$ and $w$.

## Output Format
Output $h$ lines representing the rectangle. Each character should be either `+` or `-`, alternating horizontally and wrapping to the next line.

## Sample

```input1
3 5
```

```output1
+-+-+
-+-+-
+-+-+
```

```input2
4 4
```

```output2
+-+-
-+-+
+-+-
-+-+
```

## Specification
- $1 \leq h, w \leq 10$
