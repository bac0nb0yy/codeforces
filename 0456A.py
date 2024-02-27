n = int(input())
a = []
b = []

for i in range(n):
    row = list(map(int, input().split()))
    a.append(row[0])
    b.append(row[1])
c = [[k, v] for k, v in zip(a, b)]
d = sorted(c, key=lambda x: x[1])
happy = False
for i in range(1, n):
    if d[i][0] < d[i - 1][0]:
        happy = True
        break
print("Happy Alex" if happy else "Poor Alex")
