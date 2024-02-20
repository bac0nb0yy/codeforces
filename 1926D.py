from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    h = defaultdict(int)
    for i in a:
        h[i ^ ((1 << 31) - 1)] += 1
    groups = 0
    for i in a:
        val = i ^ ((1 << 31) - 1)
        if h[val] > 0 and h[i] > 0:
            h[val] -= 1
            h[i] -= 1
            groups += 1
    print(n - groups)
