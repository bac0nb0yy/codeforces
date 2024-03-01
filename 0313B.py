s = input()
m = int(input())

dp = [0] * (len(s) + 1)

for i in range(len(s) - 1):
    dp[i + 1] = dp[i] + int(s[i] == s[i + 1])
dp[-1] = dp[-2]

for _ in range(m):
    l, r = map(int, input().split())
    print(dp[r - 1] - dp[l - 1])
