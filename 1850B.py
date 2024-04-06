for _ in range(int(input())):
    n = int(input())
    best = 0
    best_idx = 0
    for i in range(n):
        a, b = map(int, input().split())
        if a <= 10 and b > best:
            best = b
            best_idx = i + 1
    print(best_idx)
