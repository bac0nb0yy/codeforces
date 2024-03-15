def cost_flip(arr, l, r):
    return sum(arr[:l]) + sum(1 - n for n in arr[l : r + 1]) + sum(arr[r + 1 :])


n = int(input())
a = list(map(int, input().split()))

best = 0
for i in range(n):
    for k in range(i, n):
        best = max(best, cost_flip(a, i, k))
print(best)
