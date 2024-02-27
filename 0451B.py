n = int(input())
a = list(map(int, input().split()))

if len(a) == 1:
    print("yes")
    print(1, 1)
    exit()
l = 0
while l < len(a) - 1 and a[l] <= a[l + 1]:
    l += 1
r = l
while r < len(a) - 1 and a[r] >= a[r + 1]:
    r += 1
if r == l:
    print("yes")
    print(r, l)
    exit()
new = a[:l] + a[l : r + 1][::-1] + a[r + 1 :]
if new == sorted(a):
    print("yes")
    print(l + 1, r + 1)
else:
    print("no")
