## 問題描述

TEX 是由 Donald Knuth 開發的排版語言。它處理包含排版指令的原始文本，以產生高品質的文件。創建吸引人文件的一個關鍵方面是使用適當的引號。標準鍵盤只提供基本的雙引號 ("), 但 TEX 使用有方向性的雙引號 (“ ”)。挑戰在於使用 TEX 的系統，其中兩個左單引號 (``) 用於左雙引號 (“)，兩個右單引號 ('') 用於右雙引號 (”)。任務是編寫一個程序，將含有標準雙引號的文本轉換為含有 TEX 的有方向性雙引號的文本。

## 輸入格式

輸入由數行文本組成，包含偶數數量的雙引號 (") 字符。輸入以檔案結束字符結束。

## 輸出格式

輸出文本需與輸入完全一致，除了：
- 每對引號中的第一個 " 替換為兩個 ` 字符：``
- 每對引號中的第二個 " 替換為兩個 ' 字符：''

## 範例

```input1
"To be or not to be," quoth the Bard, "that
is the question".
The programming contestant replied: "I must disagree.
To `C' or not to `C', that is The Question!"
```

```output1
``To be or not to be,'' quoth the Bard, ``that
is the question''.
The programming contestant replied: ``I must disagree.
To `C' or not to `C', that is The Question!''
```

## Source

UVa Judge