for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    cur = 0
    for e in a:
        cur += e - cur % e
    print(cur)
