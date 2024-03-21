## 問題描述

實作一個函式 `insertion_sort`，該函式應該實現[插入排序法](https://en.wikipedia.org/wiki/Insertion_sort)。

## 輸入格式

輸入的第一行將包含一個整數 $N$，即陣列的大小。第二行將包含 $N$ 個整數，代表陣列 $A$ 的元素。

## 輸出格式

輸出一行包含 $N$ 個整數，即排序後的陣列。

## 範例

```input1
5
5 3 2 4 1
```

```output1
1 2 3 4 5
```

```input2
4
10 7 8 9
```

```output2
7 8 9 10
```

## 模板

| C | C++ | Python |
| -------- | -------- | -------- |
| [main.c](file://main.c) | [main.cpp](file://main.cpp) | [main.py](file://main.py) |

## Specification

- $1 \leq N \leq 10^3$
- $-10^3 \leq A_i \leq 10^3$ for $1 \leq i \leq N$
