n = int(input())
a = list(map(int, input().split()))
s = d = 0
l, r = 0, len(a) - 1
turn = 0
while l <= r:
    if a[l] < a[r]:
        best = a[r]
        r -= 1
    else:
        best = a[l]
        l += 1
    if not turn % 2:
        s += best
    else:
        d += best
    turn += 1
print(s, d)