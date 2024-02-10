from heapq import nsmallest, nlargest
from itertools import takewhile

for _ in range(int(input())):
    _, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(
        sum(a)
        + sum(
            takewhile(
                lambda x: x > 0, map(int.__sub__, nlargest(k, b), nsmallest(k, a))
            )
        )
    )
