Write a simple machine learning program. In the first training stage, we train a model. In the second prediction stage we classify inputs according to the model we trained.

## Problem Description

An image classifier classifies input images into two categories -- accept and reject. An Image is an $M \times M$ array $P$ of pixels, where each pixel $p_{i,j}$ is either zero or one. A classifier determines which category an image belongs to based on a function value $h$ of all pixels of this image. There is a weight $w_{i,j}$ for every pixel $p_{i,j}$, and the $\text{h}$ function value of an image is the sum of products of all pixel values with their corresponding weights ($\text{h}(P) = \sum_{i, j} p_{i, j} w_{i, j}$).  If the $h$ value is no less than a threshold $T$, which is $2M^2$, then the model accepts the image, otherwise it rejects the image.

The classifier starts with an initial weights of all $1$'s, then modify them according to a set of $N$ train inputs. Each input is an $M \times M$ array of $0$ or $1$'s, and has a label of either accept or reject. If the model from the current set of weights gives the same result as the label of the input image, then we do nothing. Otherwise we have two cases. In the first case the classifier accepts the input but the label is reject. Then we divide the weight of those non-zero pixel by $2$, and set the weight to $1$ if the the division gives $0$. In the second case the classifier rejects the input but the label is accept. Then we multiply the weight of those non-zero pixel by $2$.

After we train our model we use it to classify another set of $Q$ test inputs. We evaluate the $h$ function using the weights we obtained in the previous stage, and accept the input if the $h$ value is no less than the threshold, and reject the input otherwise.

## Input Format

There is one test case. Each test case has two parts.

- In the first part, the training data set contains $N$ images. The first line contains two integers $N,M$, representing that there are $N$ images which size is $M \times M$ as follows: Each image contains $M + 1$ lines. In $M + 1$ lines, the first line contains an integer $C$, representing the result of each images. In following $M$ lines, each line contains $M$ integers.

In the second part, the query data set contains $Q$ images. The first line contains an integer $Q$, representing $Q$ images as follows: Each image contains $M$ lines. Each line contains $M$ integers.

## Output Format

For each query, output one line, which contains an $0$ / $1$ integer.

## Sample

```input1
4 2
0
1 1
0 1
 
1
0 0
1 1
 
0
1 1
0 0
 
1
0 0
1 1
 
2
0 1
0 0
 
0 0
1 1
```

```output1
0
1
```

## Explain of Sample 1

1. We set all $w_{i,j}$ to $1$ and threshold $T \eq 2 M^2 = 8$.

$$
w = \begin{bmatrix}1 & 1\\1 & 1\end{bmatrix}
$$

2. Read the first image which belongs to reject group. Image classifier evaluates $h(P = \begin{bmatrix}1 & 0\\1 & 1\end{bmatrix}) = 1 + 1 + 0 + 1 = 3 \lt T$ and predicts that it belongs to reject group. We get the result of image as the same as given in input, nothing to do.

3. Read the second image which belongs to accept group. Image classifier evaluates $h(P = \begin{bmatrix}0 & 0\\1 & 1\end{bmatrix}) = 0 + 0 + 1 + 1 = 2 < T$ and predicts that it belongs to reject group. We get the result of image different from the input. The weights $w_{i, j}$ implicated in the mistake are doubled. $\forall p_{i,j} = 1: w_{i,j} \leftarrow 2\ w_{i, j}$

$$
w = \begin{bmatrix}1 & 1\\2 & 2\end{bmatrix}
$$

4. Read the third image which belongs to reject group. Image classifier evaluates $h(P = \begin{bmatrix}1 & 1\\0 & 0\end{bmatrix}) = 1 + 1 + 0 + 0 = 2 < T$ and predicts that it belongs to reject group. We get the result of image as the same as given in input, nothing to do.

5. Read the fourth image which belongs to accept group. Image classifier evaluates $h(P = \begin{bmatrix}0 & 0\\1 & 1\end{bmatrix}) = 0 + 0 + 2 + 2 = 4 < T$  and predicts that it belongs to reject group. We get the result of image different from the input.The weights $w_{i, j}$ implicated in the mistake are doubled. $\forall p_{i,j} = 1: w_{i,j} \leftarrow 2\ w_{i,j}$

$$
w = \begin{bmatrix}1 & 1\\4 & 4\end{bmatrix}
$$


## Specification

- $2 \leq N \leq 20, 1 \leq M \leq 16$
- $0 \leq Q \leq 1000$

## Source

Judge Girl