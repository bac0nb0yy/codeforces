def naive(n, a):
    count = 0
    lol = max(a)
    xd = min(a)
    l = a.copy()
    r = a.copy()
    while l[0] != lol:
        del l[0]
        count += 1
    del r[r.index(max(r))]
    r.insert(0, lol)
    while r[-1] != xd:
        del r[-1]
        count += 1
    return count


n = int(input())
a = list(map(int, input().split()))
print(naive(n, a))
