MOD = 10**9 + 7


def fact(n):
    rez = 1
    for i in range(2, n + 1):
        rez = (rez * i) % MOD
    return rez


inverse = [1] * (300_000 + 1)
for i in range(2, 300_000 + 1):
    inverse[i] = pow(i, MOD - 2, MOD)


def binom(n, k):
    numerator = fact(n)
    denominator = (fact(k) * fact(n - k)) % MOD
    return (numerator * pow(denominator, MOD - 2, MOD)) % MOD


for _ in range(int(input())):
    n, k = map(int, input().split())

    m = n
    for _ in range(k):
        x, y = map(int, input().split())
        m -= 1 + (x != y)

    rez = 0
    for c in range(m + 1):
        if not (m - c) & 1:
            perms = fact(m - c)
            overcounting = fact((m - c) // 2)
            rez = (rez + (binom(m, c) * perms * inverse[(m - c) // 2]) % MOD) % MOD

    print(rez)
