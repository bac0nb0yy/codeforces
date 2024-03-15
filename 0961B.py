n, k = map(int, input().split())
a = list(map(int, input().split()))
t = list(map(int, input().split()))

start = sum(map(int.__mul__, a, t))
rez = current = start + sum(ai for ai, ti in zip(a[:k], t[:k]) if not ti)
for i in range(k, n):
    current += (1 - t[i]) * a[i] - (1 - t[i - k]) * a[i - k]
    rez = max(current, rez)
print(rez)
