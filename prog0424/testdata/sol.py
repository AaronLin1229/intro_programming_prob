k = int(input())
for i in range(1, k + 1):
    print(" " * (i - 1), end = '')
    print('*' * (k - i + 1))
