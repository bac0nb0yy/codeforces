for _ in range(int(input())):
    n = int(input())
    for i in range(2, 30):
        val = (1 << i) - 1
        if not n % val:
            print(n // val)
            break
"""
x + 2x + 4x + 2^k-1 x = n
x + 2x + 4x + 2^k-1 x : GP formula
(2^k - 1)x = n
(2^k - 1) divise alors n
et x = n / (2^k - 1)
"""
