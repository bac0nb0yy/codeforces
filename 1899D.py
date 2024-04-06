import sys
from collections import Counter

read = sys.stdin.readline
write = sys.stdout.write
iin = lambda: int(read())
riin = lambda: range(int(read()))
miin = lambda: map(int, read().split())
lmiin = lambda: list(map(int, read().split()))

for _ in riin():
    n = iin()
    a = lmiin()
    c = Counter(a)
    ncK = 0
    for v in c.values():
        ncK += v * (v - 1) >> 1
    print(ncK + (c[1] * c[2]))
