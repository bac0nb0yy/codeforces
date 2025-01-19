# ruff: noqa: E731, E741
import math
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    n, m = mir()
    X = n - (m - 1)
    Q, R = divmod(n, m)
    print(
        (m - R) * (Q * (Q - 1) >> 1) + R * (Q * (Q + 1)) // 2,
        X * (X - 1) >> 1,
    )


if __name__ == "__main__":
    main()
