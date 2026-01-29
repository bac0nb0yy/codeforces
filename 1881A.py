# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    n, m = mir()
    x = input()
    s = input()
    rez = 0
    while s not in x:
        x = x + x
        rez += 1
        if rez > 5:
            rez = -1
            break
    print(rez)


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
