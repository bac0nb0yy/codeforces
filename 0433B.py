n = int(input())
v = list(map(int, input().split()))
v_sorted = sorted(v)

dp = [0] * n
dp_sorted = [0] * n

dp[0] = v[0]
for i in range(1, n):
    dp[i] = dp[i - 1] + v[i]

dp_sorted[0] = v_sorted[0]
for i in range(1, n):
    dp_sorted[i] = dp_sorted[i - 1] + v_sorted[i]

m = int(input())
for _ in range(m):
    t, l, r = map(int, input().split())
    if t == 1:
        print(dp[r - 1] - dp[l - 1] + v[l - 1])
    else:
        print(dp_sorted[r - 1] - dp_sorted[l - 1] + v_sorted[l - 1])
