n = int(input())
print(-1 if n & 1 else " ".join([str(i if i & 1 else i + 2) for i in range(n)]))
