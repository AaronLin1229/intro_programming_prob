n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

m = int(input())

ans = [0] * m
for num in arr:
    ans[num % m] += 1

print(*ans, sep='\n')