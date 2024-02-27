SIZE = 1000000
dp = [False] * (SIZE + 1)

dp[2020] = True
dp[2021] = True
for i in range(SIZE + 1):
    if dp[i] and i + 2020 <= SIZE:
        dp[i + 2020] = True
    if dp[i] and i + 2021 <= SIZE:
        dp[i + 2021] = True

for _ in range(int(input())):
    n = int(input())
    print("YES" if dp[n] else "NO")
