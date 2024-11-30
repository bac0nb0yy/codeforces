from random import getrandbits
from collections import defaultdict


RANDOM = getrandbits(32)


class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)

    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM


def divisors(n):
    result = set()
    for i in range(1, int(n**0.5) + 1):
        if not (n % i):
            result.add(i)
            result.add(n // i)
    return result


for _ in range(int(input())):
    k = int(input())
    a = list(map(int, input().split()))
    seen = defaultdict(bool)
    for i in a:
        seen[Wrapper(i)] = True
    divs = divisors(k - 2)
    for div in divs:
        if seen[Wrapper(((k - 2) // div))] and seen[Wrapper(div)]:
            print(div, (k - 2) // div)
            break
