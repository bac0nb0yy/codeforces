import sys

POSSIBLE = "ABC"
n = int(input())
hashmap = dict()
for k in range(len(POSSIBLE)):
    hashmap[POSSIBLE[k]] = sys.maxsize
    for i in range(k + 1, len(POSSIBLE)):
        hashmap[POSSIBLE[k] + POSSIBLE[i]] = sys.maxsize
        for j in range(i + 1, len(POSSIBLE)):
            hashmap[POSSIBLE[k] + POSSIBLE[i] + POSSIBLE[j]] = sys.maxsize

for _ in range(n):
    c, s = input().split()
    c = int(c)
    s = "".join(sorted(s))
    hashmap[s] = min(hashmap[s], c)

dp = [sys.maxsize] * (7)

"""
A = 0
B = 1
C = 2
AB = 3
AC = 4
BC = 5
ABC = 6
"""

mini = sys.maxsize

for i in range(7):
    if i < 3:
        dp[i] = hashmap[POSSIBLE[i]]
    elif i == 3:
        dp[i] = min(dp[0] + dp[1], hashmap["AB"])
    elif i == 4:
        dp[i] = min(dp[0] + dp[2], hashmap["AC"])
    elif i == 5:
        dp[i] = min(dp[1] + dp[2], hashmap["BC"])
    else:
        dp[i] = min(
            dp[3] + dp[2],
            dp[3] + dp[4],
            dp[3] + dp[5],
            dp[4] + dp[1],
            dp[4] + dp[5],
            dp[5] + dp[0],
            hashmap["ABC"],
        )
print(dp[6] if dp[6] != sys.maxsize else -1)
