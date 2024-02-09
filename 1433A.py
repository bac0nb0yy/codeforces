for _ in range(int(input())):
    x = int(input())
    print((x % 10 - 1) * 10 + sum(range(1, len(str(x)) + 1)))
