## 問題描述

[Collatz 猜想]((https://en.wikipedia.org/wiki/Collatz_conjecture#:~:text=The%20Collatz%20conjecture%20is%20one,every%20positive%20integer%20into%201.)，又稱為 $3n + 1$ 問題，涉及一個為任何正整數 $n$ 定義的序列。我們定義函數 $f(n)$ 如下：

$$
f(n) =
\begin{cases} 
n / 2 & \text{if } n \equiv 0 \mod 2\\
3n + 1 & \text{if } n \equiv 1 \mod 2 \\
\end{cases}
$$

此外，我們用賦值運算符來定義生成 Collatz 數列的過程：

$$
n \leftarrow f(n)
$$

重複這個過程，每一次的 $n$ 都是函數 $f$ 應用於前一個 $n$ 的結果，直到 $n = 1$。

任務是為給定的初始值 $n$ 模擬這個序列，並輸出序列中的所有項，直到 $n = 1$。

## 輸入格式

輸入將包含一個單獨的整數 $n$。

## 輸出格式

輸出通過重複應用函數 $f(n)$ 從輸入 $n$ 生成的整數序列，每行一個，直到 $n = 1$。

## 範例

```input1
13
```

```output1
13
40
20
10
5
16
8
4
2
1
```

```input2
5
```

```output2
5
16
8
4
2
1
```

## 規範
- $1 \leq n \leq 10^{6}$
