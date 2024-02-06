n = int(input())
h = []
a = []
ans = 0
for i in range(n):
    l = list(map(int, input().split()))
    h.append(l[0])
    a.append(l[1])
i = 0
for i in range(n):
    for j in range(n):
        if i != j and h[j] == a[i]:
            ans += 1
print(ans)
