import collections
import sys
import math
import bisect
from collections import Counter, defaultdict
import copy

read = sys.stdin.readline
write = sys.stdout.write
iin = lambda: int(read())
riin = lambda: range(int(read()))
miin = lambda: map(int, read().split())
lmiin = lambda: list(map(int, read().split()))

for _ in riin():
    n, x, y = miin()
    a = sorted(lmiin())
    rez = 0
    for i in range(x - 1):
        rez += a[i] + 2 == a[i + 1]
    if x >= 2 and (a[x - 1] + 2) % n == a[0]:
        rez += 1
    print(rez + (x - 2))
