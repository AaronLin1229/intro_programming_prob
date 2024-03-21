n = int(input())
m = int(input())
k = int(input())
dp = [1] + [0] * n
cannot_use = [False] * (n + 1)

for num in input().split():
    num = int(num)
    cannot_use[num] = True

for i in range(1, n + 1):
    if cannot_use[i] == True: continue
    for j in range(i - 1, -1, -1):
        if i - j > m: break
        dp[i] += dp[j]

print(dp[n])