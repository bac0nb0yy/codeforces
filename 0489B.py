n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
b = sorted(list(map(int, input().split())))

rez = 0
taken = [False] * m
for i in range(len(a)):
    for k in range(len(b)):
        diff = abs(a[i] - b[k])
        if diff < 2 and not taken[k]:
            rez += 1
            taken[k] = True
            break

print(min(rez, len(a), len(b)))
