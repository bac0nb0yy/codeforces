for _ in range(int(input())):
    a, b, c = map(int, input().split())
    for _ in range(5):
        mn = min(a, b, c)
        if mn == a:
            a += 1
        elif mn == b:
            b += 1
        else:
            c += 1
    print(a * b * c)
