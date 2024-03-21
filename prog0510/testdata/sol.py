n = int(input())
k = int(input())
dp = [0] * (n + 1)
cannot_use = [False] * (n + 1)

for num in input().split():
    num = int(num)
    cannot_use[num] = True

dp[0] = 1
dp[1] = 1 if cannot_use[1] == False else 0
for i in range(2, n + 1):
    if cannot_use[i]: dp[i] = 0
    else: dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])