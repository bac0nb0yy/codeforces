from math import inf

n, m = list(map(int, input().split()))
f = sorted(map(int, input().split()))
best = inf
i = 0
if m == n:
    print(0)
else:
    for i in range(m - n):
        best = min(best, f[i + n - 1] - f[i])
    print(best)
