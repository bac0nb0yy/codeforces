for _ in range(int(input())):
    w, h, n = map(int, input().split())
    sheet = 1
    while sheet < n:
        if w & 1 and h & 1:
            break
        if not w & 1:
            w //= 2
            sheet *= 2
        if not h & 1:
            h //= 2
            sheet *= 2
    print("YES" if sheet >= n else "NO")
