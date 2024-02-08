for _ in range(int(input())):
    a = sorted(list(map(int, input().split())))
    print("YES" if a[0] + a[1] == a[2] else "NO")