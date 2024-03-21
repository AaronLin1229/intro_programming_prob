## 問題描述

撰寫一個程式來計算有多少整數可以分別表示為 $M \cdot k, M \cdot k + 1, \dots, M \cdot k + (M - 1)$。

## 輸入格式

第一行包含一個整數 $N$，代表輸入整數的數量。接下來的 $N$ 行，每行包含一個輸入整數。最後一行包含 $M$。

## 輸出格式

輸出可以表示為 $M \cdot k, M \cdot k + 1, \dots, M \cdot k + (M - 1)$ 的整數數量。

## 範例

```input1
5
1
2
3
4
5
3
```

```output1
1
2
2
```

```input2
10
3
1
4
1
5
9
2
6
5
3
3
```

```output2
4
3
3
```

## 規格

- $1 \leq N \leq 10^5$
- $1 \leq M \leq 2 \times 10^5$
- 所有陣列元素皆為 `int`.


## Source

Judge Girl