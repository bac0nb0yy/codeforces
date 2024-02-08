import sys

n, a, b, c = map(int, input().split())

dp = [-sys.maxsize] * (n + 1)
dp[0] = 0
for i in range(1, n + 1):
    for k in (a, b, c):
        if i >= k:
            dp[i] = max(dp[i], dp[i - k] + 1)
print(dp[n])
