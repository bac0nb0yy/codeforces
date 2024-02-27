for _ in range(int(input())):
    n, x = map(int, input().split())
    floor = 1
    numbers = 2
    while numbers < n:
        numbers = floor * x + 2
        floor += 1
    print(floor)
