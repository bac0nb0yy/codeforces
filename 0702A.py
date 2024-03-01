n = int(input())
a = list(map(int, input().split()))

maxi = cur = 1
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        cur += 1
        maxi = max(maxi, cur)
    else:
        cur = 1
print(maxi)
