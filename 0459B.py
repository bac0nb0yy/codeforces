from math import comb


n = int(input())
b = list(map(int, input().split()))

mn_cnt = 0
mx_cnt = 0

mn = 1 << 30
mx = 0

for x in b:
    if x < mn:
        mn = x
        mn_cnt = 1
    elif x == mn:
        mn_cnt += 1
    if x > mx:
        mx = x
        mx_cnt = 1
    elif x == mx:
        mx_cnt += 1

if mn == mx:
    print(0, comb(n, 2))
else:
    print(mx - mn, mn_cnt * mx_cnt)
