from collections import Counter
from heapq import heappop, heappush

multiset = Counter()
earliest = []
latest = []
for _ in range(int(input())):
    o, *x = input().split()
    l, r = map(int, x)
    if o == "+":
        multiset[l, r] += 1
        if multiset[l, r] == 1:
            heappush(earliest, (r, l))
            heappush(latest, (-l, -r))
    else:
        multiset[l, r] -= 1
        if multiset[l, r] == 0:
            del multiset[l, r]
    while earliest and (earliest[0][1], earliest[0][0]) not in multiset:
        heappop(earliest)
    while latest and (-latest[0][0], -latest[0][1]) not in multiset:
        heappop(latest)
    print("yEs" if earliest and earliest[0][0] < -latest[0][0] else "nO")
