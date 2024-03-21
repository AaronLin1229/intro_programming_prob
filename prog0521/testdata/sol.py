n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    max_num = -2e6
    for j in range(m):
        max_num = max(max_num, arr[i][j])
    print(max_num, end = ' ')

print()

for j in range(m):
    min_num = 2e6
    for i in range(n):
        min_num = min(min_num, arr[i][j])
    print(min_num, end = ' ')

print()