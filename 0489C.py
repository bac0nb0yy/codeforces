m, s = map(int, input().split())

if s > m * 9 or (s == 0 and m != 1):
    print("-1 -1")
elif m == 1:
    print(s, s)
else:

    def can(m, s):
        return s >= 0 and s <= 9 * m

    s_minn = s
    s_maxn = s
    minn = ""
    maxn = ""
    for i in range(m):
        for k in range(10):
            if (i or k) and can(m - i - 1, s_minn - k):
                minn += str(k)
                s_minn -= k
                break
        for k in range(9, -1, -1):
            if (i or k) and can(m - i - 1, s_maxn - k):
                maxn += str(k)
                s_maxn -= k
                break
    print(minn, maxn)
