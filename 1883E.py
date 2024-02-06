import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    rez = op = 0
    for i in range(1, len(a)):
        op = (
            max(op - (a[i] // a[i - 1]).bit_length() + 1, 0)
            if a[i] >= a[i - 1]
            else op + ((a[i - 1] - 1) // a[i]).bit_length()
        )
        rez += op
    print(rez)
