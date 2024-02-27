for _ in range(int(input())):
    *t, n = map(int, input().split())
    mx = max(t)
    diff = sum((mx - i for i in t))
    print("YES" if n >= diff and not (n - diff) % 3 else "NO")
