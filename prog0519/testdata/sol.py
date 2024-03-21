n = int(input())
arr = list(map(int, input().split()))
k = int(input())

for i in range(n):
    for j in range(i + 1, n):
        if arr[i] + arr[j] == k:
            print(i + 1, j + 1)
