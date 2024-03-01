for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    odd = sum([i % 2 for i in a])
    print("YES" if not odd & 1 else "NO")
