## Problem Description

TEX is a typesetting language developed by Donald Knuth. It processes source text with typesetting instructions to produce high-quality documents. A key aspect of creating appealing documents is the use of proper quotation marks. Standard keyboards only provide the basic double-quote ("), but TEX uses oriented double-quotes (“ ”). The challenge is to use TEX's system where two left-single-quotes (``) are used for a left-double-quote (“) and two right-single-quotes ('') for a right-double-quote (”). The task is to write a program that converts text with standard double-quotes into text with TEX's oriented double-quotes.

## Input Format

The input consists of several lines of text containing an even number of double-quote (") characters. The input ends with an end-of-file character.

## Output Format

Output the text exactly as input except:
- The first " in each pair is replaced by two ` characters: ``
- The second " in each pair is replaced by two ' characters: ''

## Sample

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