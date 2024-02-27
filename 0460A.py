n, m = map(int, input().split())
day = 0
while n != 0:
    if not day % m:
        n += 1
    n -= 1
    day += 1
print(day - 1)
