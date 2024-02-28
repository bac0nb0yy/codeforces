for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ma = min(a)
    mb = min(b)
    count = 0
    for i in range(n):
        both = min(a[i] - ma, b[i] - mb)
        count += both + (a[i] - both - ma) + (b[i] - both - mb)
    print(count)
