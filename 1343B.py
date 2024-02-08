for _ in range(int(input())):
    n = int(input())
    if n & 2:
        print("NO")
    else:
        print("YES")
        print(*range(2, n + 1, 2), *range(1, n - 1, 2), n - 1 + (n >> 1))
