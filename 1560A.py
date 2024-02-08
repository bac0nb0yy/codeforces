MAX = 1_000
cache = []

k = 1
for i in range(MAX + 1):
    while not k % 3 or k % 10 == 3:
        k += 1
    cache.append(k)
    k += 1

for _ in range(int(input())):
    n = int(input())
    print(cache[n - 1])