n = int(input())
A = list(map(int, input().split()))

min_diff = float('inf')
for i in range(1, n):
    min_diff = min(min_diff, A[i] - A[i - 1])

print(min_diff)
