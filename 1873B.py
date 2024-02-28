import math

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ma = min(a)
    for i in range(len(a)):
        if a[i] == ma:
            a[i] += 1
            break
    print(math.prod(a))
