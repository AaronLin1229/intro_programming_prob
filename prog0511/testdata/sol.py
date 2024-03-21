n = int(input())
m = int(input())
dp = [1] + [0] * n

for i in range(1, n + 1):
    for j in range(i - 1, -1, -1):
        if i - j > m: break
        dp[i] += dp[j]

print(dp[n])