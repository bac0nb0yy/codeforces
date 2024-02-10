for _ in range(int(input())):
    n = int(input())
    rez = n // 3
    mod = n % 3
    print(rez + (mod == 1), rez + (mod == 2))
