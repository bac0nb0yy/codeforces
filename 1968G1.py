def z_func(s):
    n = len(s)
    z = [0] * n
    for i in range(1, n):
        j = z[i - 1]
        while j > 0 and s[i] != s[j]:
            j = z[j - 1]
        if s[i] == s[j]:
            j += 1
        z[i] = j
    return z


def f(z, size):
    n = len(z)
    cnt = 1
    i = size
    while i < n:
        if z[i] >= size:
            cnt += 1
            i += size
        else:
            i += 1
    return cnt


for _ in range(int(input())):
    n, k, k = map(int, input().split())
    s = input()
    z = z_func(s)
    l, r = 0, n + 1
    while r - l > 1:
        mid = (l + r) // 2
        if f(z, mid) >= k:
            l = mid
        else:
            r = mid
    print(l)
