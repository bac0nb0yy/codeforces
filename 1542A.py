for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(
        "YES"
        if len([i for i in a if i % 2]) == len([i for i in a if not i % 2])
        else "NO"
    )
