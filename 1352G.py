for _ in range(int(input())):
    n = int(input())
    if n <= 3:
        print("-1")
    elif n == 4:
        print("3 1 4 2")
    elif n == 5:
        print("1 3 5 2 4")
    elif n == 6:
        print("1 3 5 2 6 4")
    else:
        rez = list(range(1, n + 1, 2))
        rez.append(rez[-1] - 3)
        if n & 1:
            rez.append(rez[-1] + 2)
            rez.append(rez[-1] - 4)
        else:
            rez.append(rez[-1] + 4)
            rez.append(rez[-1] - 2)
            rez.append(rez[-1] - 4)
        rez.extend(list(range(rez[-1] - 2, 0, -2)))
        print(*rez)


# 3 1 4 2
# 1 3 5 2 4
# 1 3 5 2 6 4
# 1 3 5 7 4 6 2
# 1 3 5 7 4 8 6 2
# 1 3 5 7 9 6 8 4 2
# 1 3 5 7 9 6 a 8 4 2
