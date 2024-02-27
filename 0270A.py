for _ in range(int(input())):
    a = int(input())
    print("YES" if not 360 % (180 - a) else "NO")
