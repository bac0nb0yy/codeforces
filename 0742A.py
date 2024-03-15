import math

n = int(input())

# on peut décomposer k^n en : k^y * k^x * k^z...
# tant que x + y + z + ... = n
# (8^10) % 10 = 4
# (8^(10^k)) % 10 = 6 avec k > 1

rez = 1
while n >= 10:
    rez = (rez * (4 + 2 * (n >= 100))) % 10
    n -= 10 ** int(math.log(n, 10))

print(rez * (8**n) % 10)
