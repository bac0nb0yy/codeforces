from math import isqrt

SIZE = 1_000_001
sieve = [True] * SIZE
sieve[0] = sieve[1] = False
for i in range(2, isqrt(SIZE) + 1):
    if sieve[i]:
        for j in range(i * i, SIZE, i):
            sieve[j] = False

input()
for n in map(int, input().split()):
    i = isqrt(n)
    print("YES" if i * i == n and sieve[i] else "NO")
