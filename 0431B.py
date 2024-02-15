import itertools


def calculate_happiness(dp, permutation):
    happiness = 0
    for i in range(4):
        for k in range(i, 4, 2):
            happiness += dp[permutation[k]][permutation[k + 1]]
            happiness += dp[permutation[k + 1]][permutation[k]]
    return happiness


dp = []
for _ in range(5):
    dp += [list(map(int, input().split()))]

best = 0
for perm in list(itertools.permutations(range(5))):
    best = max(best, calculate_happiness(dp, perm))

print(best)
