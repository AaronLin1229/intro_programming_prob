## 問題描述

撰寫一個 C/C++ 或 Python 函數，用來計算給定陣列中正數和負數的數量。

C/C++ 函數應為：

```cpp
void count_pos_neg(int arr[], int n, int res[2])
```

其中 `arr[]` 是我們要計算正數和負數的陣列， `n` 是 `arr[]` 的大小。我們希望將結果儲存在 `res` 中，其中 `res[0]` 儲存正數的數量， `res[1]` 儲存負數的數量。

Python 函數應為：

```Python
def count_pos_neg(arr: list[int]) -> list[int]
```

其中 `arr` 是我們要計算正數和負數的陣列。我們將以大小為 2 的 list 形式回傳正數和負數的數量，其中第一個元素是正數的數量，第二個元素是負數的數量。

## 輸入格式

第一行包含單一整數 $n$（陣列的大小）。
第二行包含 $n$ 個用空格分隔的整數，代表陣列 $A$ 的元素。

## 輸出格式

輸出兩個用空格分隔的整數。第一個整數是陣列中正數的數量，第二個整數是負數的數量。

## 範例

```input1
5
-1 2 3 -4 5
```

```output1
3 2
```

```input2
4
-3 -2 -1 0
```

```output2
0 3
```

## 模板

| C | C++ | Python |
| -------- | -------- | -------- |
| [main.c](file://main.c) | [main.cpp](file://main.cpp) | [main.py](file://main.py) |

## 規格

- $1 \leq n \leq 10^4$
- $-10^9 \leq A_i \leq 10^9$, where $1 \leq i \leq n$
