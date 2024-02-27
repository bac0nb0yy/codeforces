CACHE = [10**k for k in range(9)]

for _ in range(int(input())):
    n = int(input())
    count = 0
    for i in range(1, 10):
        for k in range(len(CACHE)):
            tot = i * sum(CACHE[: k + 1])
            if tot <= n:
                count += 1
    print(count)
