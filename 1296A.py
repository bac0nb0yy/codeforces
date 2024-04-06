for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    odd = sum(i & 1 for i in a)
    print("NO" if (odd == 0 or odd == n) and not sum(a) & 1 else "YES")
