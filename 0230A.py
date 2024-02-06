import sys

s, n = map(int, input().split())
a = sorted(list(map(int, input().split())) for _ in range(n))
for x, y in a:
    if x >= s:
        print("NO")
        sys.exit()
    s += y
print("YES")
