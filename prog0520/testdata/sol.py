n = int(input())
arr = list(map(int, input().split()))

max_num = -2000000000
for i in range(n):
    _sum = 0
    for j in range(i, n):
        _sum += arr[j]
        max_num = max(max_num, _sum)

print(max_num)
