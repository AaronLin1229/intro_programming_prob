## 題目描述
撰寫一個程式，將單一字元 `ch` 分類為四個類別之一。字元的類別是基於它的大小寫和它是否為母音字母。

- 如果 `ch` 是大寫母音，印出 `<ch> is class A`。
- 如果 `ch` 是小寫母音，印出 `<ch> is class B`。
- 如果 `ch` 是大寫子音，印出 `<ch> is class C`。
- 否則，印出 `<ch> is class D`。

母音字母是字符 'A', 'E', 'I', 'O', 'U' 及其小寫。

## 輸入格式
單行包含字元 `ch`。

## 輸出格式
單行陳述字元的類別。

## 樣本

```input1
A
```

```output1
A is class A
```

```input2
b
```

```output2
b is class D
```

## 規範
- `ch` 是英文字母
