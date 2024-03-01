n = int(input())
print(sum(not (n - i) % i for i in range(1, n // 2 + 1)))
