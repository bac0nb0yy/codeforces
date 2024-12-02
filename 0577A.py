from collections import defaultdict
from math import isqrt, sqrt


def find_div(x):
    rez = list()
    for i in range(2, isqrt(x) + 1, 1):
        if x % i == 0:
            rez.append(x // i)
            rez.append(i)
    return sorted([1] + rez + [x])


n, x = map(int, input().split())
divs = find_div(x)

cnt = 0

seen = defaultdict(bool)
for div in divs:
    if x // div <= n and div <= n and x // div not in seen and div not in seen:
        if div == sqrt(x):
            cnt += 1
        else:
            cnt += 2
        seen[x // div] = True
        seen[div] = True

print(cnt)
