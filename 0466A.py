n, m, a, b = map(int, input().split())
s = 0
left = n
if b / m <= a:
    s += (b * (n // m))
    left -= (n // m) * m
s += min(a * left, int(left / m + 0.5) * b)
print(s)