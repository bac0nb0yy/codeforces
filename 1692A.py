for _ in range(int(input())):
    a,b,c,d = map(int, input().split())
    print(1 * (b > a) + 1 * (c > a) + 1 * (d > a))