n = int(input())
dp = [0] * (n + 1)
for i in range(2, n + 1, 2):
    dp[i] = max(dp[i - 2] * 2, 2)
print(dp[n])
