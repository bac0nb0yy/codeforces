for _ in range(int(input())):
    a, b = map(int, input().split())
    print(
        0
        if a == b
        else 1
        if (a < b and (b - a) & 1) or (a > b and not (a - b) & 1)
        else 2
    )
