from heapq import heappop, heappush
import sys

n = int(sys.stdin.readline())
rez = cur = 0
h = []
for x in map(int, sys.stdin.readline().split()):
    if x + cur >= 0:
        if x < 0:
            heappush(h, x)
        rez += 1
        cur += x
    elif h and x > h[0]:
        cur += x - h[0]
        heappop(h)
        heappush(h, x)
print(rez)
