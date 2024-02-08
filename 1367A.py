for _ in range(int(input())):
    b = input()
    a = b[:2]
    for i in range(3, len(b), 2):
        a += b[i]
    print(a)