for _ in range(int(input())):
    x, y, n = map(int, input().split())
    ans = n - n % x + y
    print(ans if ans <= n else n - n % x - (x - y))
