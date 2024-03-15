n = int(input())

dp = [0] * 10
dp[0] = 1
dp[1] = 8
dp[2] = 4
dp[3] = 2
dp[4] = 6
dp[5] = 8
dp[6] = 4
dp[7] = 2
dp[8] = 6
dp[9] = 8


# on peut décomposer k^n en : k^y * k^x * k^z...
# tant que x + y + z + ... = n

rez = 1
while n >= 10:
    rez = (rez * 4) % 10
    n -= 10

print((rez * dp[n]) % 10)
