## 問題描述

寫一個程式來進行字串的「融合」。融合類似於字串串接，但如果它們相同的話，它會結合第一個字串的後綴和第二個字串的前綴。例如，如果你將 `abcd` 和 `cdef` 融合，那麼你將得到 `abcdef`。此外，融合將嘗試盡可能多地融合字符。例如，如果你將 `abccc` 和 `cccde` 融合，那麼你將得到 `abcccde`，而不是 `abccccde` 或 `abcccccde`。

## 輸入格式

輸入包含一系列（至少兩個）非空的由小寫字母組成的字串，你需要將下一個字串融合到前一次融合的結果中。你必須處理所有字串直到 EOF。每個字串以及所有中間結果的長度都不超過 127 個字符。

## 輸出格式

最終融合結果。

## 範例

```input1
a
b
c
bcde
bcde
cdefghi
ghi
ghi
ghijk
abcdefghijklmn
zzz
zzzz
abc
```

```output1
abcdefghijklmnzzzzabc
```

## Source

Judge Girl