# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    n, k = mir()
    a = sorted(lmir())
    groups = []
    i = 0
    while i < n:
        sub = [a[i]]
        i += 1
        while i < n:
            if abs(a[i] - a[i - 1]) <= k:
                sub.append(a[i])
                i += 1
            else:
                break
        groups.append(sub)
    mx = max(range(len(groups)), key=lambda i: len(groups[i]))
    rez = sum(len(groups[i]) for i in range(len(groups)) if i != mx)
    print(rez)


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
