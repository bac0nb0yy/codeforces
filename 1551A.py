for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(1, 0)
    elif n == 2:
        print(0, 1)
    else:
        rez = n // 3
        if rez * 3 != n:
            if n % rez == 1:
                print(rez + 1, rez)
            else:
                print(rez, rez + 1)
        else:
            print(rez, rez)
