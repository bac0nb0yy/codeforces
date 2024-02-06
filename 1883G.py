from bisect import bisect
from collections import deque
import sys


def f(a, b, n):
    a = a.copy()
    b = b.copy()
    idx = bisect(a, n)
    a.insert(idx, n)
    rez = 0
    while a:
        if a[-1] < b[-1]:
            b.pop()
        else:
            rez += 1
            b.popleft()
        a.pop()
    return rez


for _ in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().split())
    a = deque(sorted(map(int, sys.stdin.readline().split())))
    b = deque(sorted(list(map(int, sys.stdin.readline().split()))))
    f1 = f(a, b, 1)
    fm = f(a, b, m)
    if f1 == fm:
        print(f1 * m)
    else:
        lo = 1
        hi = m
        while lo < hi:
            mi = lo + hi >> 1
            if f(a, b, mi) == f1:
                lo = mi + 1
            else:
                hi = mi
        print(fm * m - lo + 1)
