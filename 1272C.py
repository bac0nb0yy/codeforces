n, k = map(int, input().split())
s = input()
letters = input().split()

dp = [0] * n
dp[0] = s[0] in letters
for i in range(1, n):
    if s[i] in letters:
        dp[i] = 1 + dp[i - 1]
print(sum(dp))
