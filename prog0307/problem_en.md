## Problem Description
Given two times in 24-hour format (`hh mm``), calculate the time difference between them. The time is given as hours and minutes, and the difference should be printed out also in hours and minutes.

## Input Format
The input contains two lines. Each line consists of two integers $H$ and $M$, representing the hour and the minute of a time.

## Output Format
Output the time difference in the format `h m`, where `h` is the hours and `m` is the minutes. If the second time is earlier than the first time, calculate the time difference between the two consective day, while the first time represents the first day, the second time represents the second day.

There is no need to fill leading zeros in output.

## Sample

```input1
10 30
12 45
```

```output1
2 15
```

```input2
23 59
00 01
```

```output2
0 2
```

## Specification
- $0 \leq H \leq 23$
- $0 \leq M \leq 59$
