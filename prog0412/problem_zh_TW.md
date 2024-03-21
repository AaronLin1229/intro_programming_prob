## 問題描述

給定兩個正整數 $a$ 和 $b$，使用以下定義計算兩個數字的最大公因數 $\gcd(a, b)$：

$$
\gcd(a, b) =
\begin{cases}
a & \text{if } b = 0\\
\gcd(b, a \bmod b) & \text{otherwise}
\end{cases}
$$

注意 $\gcd()$ 運算滿足交換律，即 $\gcd(a, b) = \gcd(b, a)$。

## 輸入格式

兩個正整數 $a$ 和 $b$，以空白間隔。

## 輸出格式

代表 $a$ 和 $b$ 的最大公因數的單個整數。

## 範例

```input1
12 15
```

```output1
3
```

```input2
101 10
```

```output2
1
```

## 規範
- $1 \leq a, b \leq 10^{8}$
