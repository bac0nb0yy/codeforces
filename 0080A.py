import math

SIZE = 50
sieve = [True] * (SIZE + 1)
sieve[0] = sieve[1] = False

for i in range(2, math.isqrt(SIZE) + 1):
    if sieve[i]:
        for k in range(i * i, SIZE + 1, i):
            sieve[k] = False


def good(n, m):
    for i in range(n + 1, SIZE + 1):
        if sieve[i]:
            return i == m
    return False


n, m = map(int, input().split())
print("YNEOS"[good(n, m) ^ 1 :: 2])
