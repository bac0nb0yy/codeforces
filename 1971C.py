for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    rez = []
    for i in range(1, 13):
        if i == a or i == b:
            rez.append("r")
        elif i == c or i == d:
            rez.append("b")
    print("NO" if "".join(rez) in ("rrbb", "bbrr", "rbbr", "brrb") else "YES")
