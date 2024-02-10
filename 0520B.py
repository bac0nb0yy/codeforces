import sys

SIZE = 20_000

n, m = map(int, input().split())

dp = list(reversed(range(n + 1))) + [sys.maxsize] * (SIZE - n + 1)
dp[n] = 0


def find_next_good(dp, n):
    for i in range(n, SIZE + 1):
        if dp[i] != sys.maxsize:
            return i


for k in range(1, m + 1):
    next_index = find_next_good(dp, k)
    dp[k] = min(dp[next_index] + next_index - k, dp[k])
    dp[k * 2] = min(dp[k * 2], dp[k] + 1)

print(dp[m])
