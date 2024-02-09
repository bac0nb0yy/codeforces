from math import gcd

x, y = map(int, input().split())

numerator = 6 - max(x, y) + 1
d = gcd(numerator, 6)
print(f"{numerator//d}/{6//d}")
