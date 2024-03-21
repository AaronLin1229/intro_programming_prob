## 問題描述

計算二項式係數 $C^n_k$，這是從 $n$ 個元素的集合中選擇 $k$ 個元素的方法數，不考慮選擇的順序。二項式係數定義為：

$$
C^n_k = \frac{n!}{k!(n-k)!}
$$

其中 $n!$ 表示 $n$ 的階乘。

## 輸入格式

輸入包含兩個整數，$n$ 和 $k$，由一個空格分隔。

## 輸出格式

一個整數，代表 $a$ 和 $b$ 的總和。

## 模板

| C | C++ | Python |
| -------- | -------- | -------- |
| [main.c](file://main.c) | [main.cpp](file://main.cpp) | [main.py](file://main.py) |

## 範例

```input1
5 2
```

```output1
10
```

```input2
6 3
```

```output2
20
```

## 模板

| C | C++ | Python |
| -------- | -------- | -------- |
| [main.c](file://main.c) | [main.cpp](file://main.cpp) | [main.py](file://main.py) |

## 規格

- $n$：範圍 $[0, 12]$ 內的整數
- $k$：範圍 $[0, n]$ 內的整數