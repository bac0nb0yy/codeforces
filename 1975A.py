for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(1, n - 1):
        if a[i - 1] > a[i] < a[i + 1]:
            print("NO")
            break
    else:
        print("YES")