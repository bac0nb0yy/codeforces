from collections import Counter
import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    total = Counter(a)
    rez = start = 0
    c = Counter()
    for x in a:
        c[x] += 1
        start += c[x] == total[x]
    for x in a:
        rez += (c[x] == total[x]) * start
        c[x] -= 1
        start -= c[x] == 0
    print(rez)
