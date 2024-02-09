for _ in range(int(input())):
    n = int(input())
    print(["NO", "YES"][n & (n - 1) > 0])
