def naive(n, k):
    l = [*range(1, n + 1, 2), *range(2, n + 1, 2)]
    return l[k - 1]


def smart(n, k):
    if 2 * k <= n + 1:
        return k * 2 - 1
    else:
        return (k - (n + 1) // 2) * 2


n, k = map(int, input().split())
print(smart(n, k))
