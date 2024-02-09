n, k = map(int, input().split())
h = list(map(int, input().split()))

best = sum(h[:k])
min_index = 0
val = best
for i in range(1, len(h) - k + 1):
    val = val - h[i - 1] + h[i + k - 1]
    if val < best:
        best = val
        min_index = i

print(min_index + 1)
