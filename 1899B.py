import math


def find_divisors(n):
    result = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            result.add(i)
            result.add(n // i)
    return list(result)


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    divisors = find_divisors(n)
    best = 0
    for i in divisors:
        mini = math.inf
        maxi = -math.inf
        k = 0
        while k < len(a) - i + 1:
            cur = 0
            j = 0
            while j < i:
                cur += a[k + j]
                j += 1
            k += i
            mini = min(mini, cur)
            maxi = max(maxi, cur)
        best = max(best, maxi - mini)
    print(best)
