for _ in range(int(input())):
    n = int(input())
    l1 = input()
    l2 = input()
    print(
        "YES"
        if all(
            x == y for x, y in zip(l1, l2) if x not in ("G", "B") or y not in ("G", "B")
        )
        else "NO"
    )
