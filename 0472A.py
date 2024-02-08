n = int(input())
MAX = 500_000

sieves = [True] * (MAX + 1)
p = 2
while p * p <= MAX:
    if sieves[p]:
        for i in range(p * p, MAX + 1, p):
            sieves[i] = False
    p += 1

x = n // 2
y = (n // 2) + (n & 1)
best = max(x,y)
while sieves[x] or sieves[y]:
    if best == x:
        x -= 1
        y += 1
    else:
        x -= 1
        y += 1
print(x,y)