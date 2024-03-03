from collections import deque
import sys

for _ in range(int(input())):
    n, k, x = map(int, input().split())
    a = deque(sorted(list(map(int, input().split()))))
    dp = [-sys.maxsize] * (n)
    dp[0] = a[0]
    for i in range(1, n):
        dp[i] = dp[i - 1] + a[i]
    ans = -sys.maxsize
    for i in range(k):
        ans = max(ans, dp[n - 1] - 2 * dp[min(i + x, n - 1)] + dp[i])
    print(ans)
