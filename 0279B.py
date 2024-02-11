n, t = map(int, input().split())
a = list(map(int, input().split()))

dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = dp[i - 1] + a[i - 1]

rez = 0
for i in range(1, n + 1):
    l, r = i - 1, n
    while l < r:
        mid = (l + r + 1) // 2
        interval = dp[mid] - dp[i - 1]
        if interval <= t:
            l = mid
        else:
            r = mid - 1
    rez = max(rez, r - i + 1)

print(rez)
