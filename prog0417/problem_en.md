## Problem Description
You've been tasked with developing a program to encrypt multiple lines of text using a simple Caesar Cipher. The Caesar Cipher is a type of substitution cipher where each letter in the plaintext is 'shifted' a certain number of places down or up the alphabet. For this task, a positive shift means shifting the characters forward (e.g., A with a shift of 3 becomes D) and a negative shift means shifting the characters backward (e.g., D with a shift of 3 becomes A). The case of the letters should be preserved, and non-alphabetical characters should remain unchanged.

Your program should be able to read a number $k$ indicating the shift amount on the first line, followed by multiple lines of strings that need to be encrypted.

## Input Format
The first line of the input contains an integer $k$, the number of positions each letter in the text should be shifted.
From the second line onwards, each line contains a string of text that needs to be encrypted.

## Output Format
Output the encrypted text, preserving the format of the input text. Each encrypted line of text should correspond to each line of the input text.

## Sample

```input1
3
Hello, World!
Zebra-123
```

```output1
Khoor, Zruog!
Cheud-123
```

```input2
-1
abc XYZ
```

```output2
zab WXY
```

## Specification
- The shift value $k$ will satisfy $-100 \leq k \leq 100$.
- The length of each line of the string will be at most 1000 characters.
