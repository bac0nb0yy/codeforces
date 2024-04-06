for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(
        "YES" if sum(i for i in a if i & 1) < sum(i for i in a if not i & 1) else "NO"
    )
