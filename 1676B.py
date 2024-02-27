for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ma = min(a)
    print(sum(i - ma for i in a))
