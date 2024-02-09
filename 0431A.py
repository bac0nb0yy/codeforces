a = list(map(int, input().split()))
print(sum(a[int(i) - 1] for i in input()))
