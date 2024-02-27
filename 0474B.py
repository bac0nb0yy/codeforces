import bisect

n = int(input())
a = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))

prefix = [a[0]]
for i in a[1:]:
    prefix.append(prefix[-1] + i)

for i in q:
    print(bisect.bisect_left(prefix, i) + 1)
