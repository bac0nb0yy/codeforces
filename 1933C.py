for _ in range(int(input())):
    a, b, z = map(int, input().split())
    a_possible = [1]
    b_possible = [1]
    cur = a
    while cur <= z:
        a_possible.append(cur)
        cur *= a
    cur = b
    while cur <= z:
        b_possible.append(cur)
        cur *= b
    good = set()
    for i in a_possible:
        for j in b_possible:
            l, r = 0, z + 1
            while l < r:
                mid = (l + r) // 2
                val = mid * i * j
                if val == z and mid not in good:
                    good.add(mid)
                    break
                elif val > z:
                    r = mid
                else:
                    l = mid + 1
    print(len(good))
