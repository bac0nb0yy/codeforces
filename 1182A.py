n = int(input())
dp = [0] * (n + 1)
dp[0] = 1
for i in range(2, n + 1, 2):
    dp[i] = dp[i - 2] * 2
print(dp[n])
