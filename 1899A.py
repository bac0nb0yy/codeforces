for _ in range(int(input())):
    n = int(input())
    print("First" if not (n + 1) % 3 or not (n - 1) % 3 else "Second")
