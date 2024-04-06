for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    best = cur = a[0]
    for i in range(1, len(a)):
        if a[i] & 1 != a[i - 1] & 1:
            cur = max(cur + a[i], a[i])
        else:
            cur = a[i]
        best = max(best, cur)
    print(best)
