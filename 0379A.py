a, b = map(int, input().split())
c = 0
d = a
while d >= b:
    c += d // b
    d = (d % b) + (d // b)
print(a + c)
