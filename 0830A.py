import sys


def cost(person, key, office):
    return abs(person - key) + abs(key - office)


n, k, p = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

dp = [[sys.maxsize for _ in range(n + 1)] for _ in range(k + 1)]
dp[0][0] = 0

for i in range(k):
    for j in range(n + 1):
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])

        if j < n:
            dp[i + 1][j + 1] = min(dp[i + 1][j + 1], max(dp[i][j], cost(a[j], b[i], p)))

print(dp[k][n])
