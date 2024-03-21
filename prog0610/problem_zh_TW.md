## 問題描述

回想 prog0528. Game of Life。現在，你應該為生命遊戲的 $n \times n$ 棋盤編寫兩個函數：

1. step(board, n)：這個函數將模擬遊戲的一輪。
2. print(board, n)：這個函數將列印棋盤的狀態。

## 輸入格式

- 第一行包含一個整數 $n$，網格的大小。
- 接下來的 $n$ 行每行包含 $n$ 個數字，代表網格的初始配置。0 代表死細胞，1 代表活細胞。
- 最後一行包含一個整數 $m$，模擬的輪數。

## 輸出格式

輸出 $n$ 行，每行包含 $n$ 個字元，代表 $k$ 輪後的網格配置。

## 模板

| C | C++ | Python |
| -------- | -------- | -------- |
| [main.c](file://main.c) | [main.cpp](file://main.cpp) | [main.py](file://main.py) |

## 範例

```input1
3
0 1 0
0 0 1
1 0 1
1
```

```output1
0 0 0
0 0 1
0 1 0
```

```input2
4
1 0 1 0
0 0 0 0
0 1 0 1
0 0 0 0
2
```

## 模板

| C | C++ | Python |
| -------- | -------- | -------- |
| [main.c](file://main.c) | [main.cpp](file://main.cpp) | [main.py](file://main.py) |

## 規格

- $1 \leq n \leq 128$
- $0 \leq m \leq 100$

