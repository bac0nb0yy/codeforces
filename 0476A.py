n, m = map(int, input().split())
if m > n:
    print(-1)
else:
    for i in range(n // 2 + (n & 1), n + 1):
        if not i % m:
            print(i)
            break
