for _ in range(int(input())):
    a, b = map(int, input().split())
    xk, yk = map(int, input().split())
    xq, yq = map(int, input().split())
    dirs = [(b, a), (a, b), (a, -b), (b, -a), (-b, -a), (-a, -b), (-a, b), (-b, a)]
    posk = []
    posq = []
    for x, y in dirs:
        k = [xk + x, yk + y]
        q = [xq + x, yq + y]
        if k not in posk:
            posk.append(k)
        if q not in posq:
            posq.append(q)
    rez = 0
    for pos in posk:
        if pos in posq:
            rez += 1
            continue
    print(rez)
