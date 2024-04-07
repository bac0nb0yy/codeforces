from collections import defaultdict


def find_mex(array):
    mex = 0
    for i in sorted(set(array)):
        if i != mex:
            break
        mex += 1
    return mex


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    mex_arr = find_mex(a)
    start = 0
    seen = defaultdict(int)
    mex = 0
    for i in range(len(a)):
        seen[a[i]] = True
        while seen[mex]:
            mex += 1
        if mex == mex_arr:
            start = i
            break

    seen = defaultdict(bool)
    mex = 0
    find = False
    for i in range(start + 1, len(a)):
        seen[a[i]] = True
        while seen[mex]:
            mex += 1
        if mex == mex_arr:
            find = True
            break

    print(-1 if not find else 2)
    if find:
        print(1, start + 1)
        print(start + 2, n)
