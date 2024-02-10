from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    d = Counter(a)

    tot = d[1] + 2 * d[2]
    if tot & 1:
        print("NO")
    else:
        s = tot // 2
        print("YES" if not s & 1 or (s & 1 and d[1]) else "NO")
