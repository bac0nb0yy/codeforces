for _ in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))

    print(*[b[i // 2] if not i & 1 else b[n - (i // 2) - 1] for i in range(n)])
