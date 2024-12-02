# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve(n, k):
    if k > n:
        return None
    if n & 1 == k & 1:
        res = [1] * k
        res[0] = n - (k - 1)
        return res
    if k << 1 <= n and n & 1 == 0:
        res = [2] * k
        res[0] = n - ((k - 1) << 1)
        return res
    return None


def main():
    for _ in rir():
        n, k = mir()
        rez = solve(n, k)
        if rez:
            print("YES")
            print(*rez)
        else:
            print("NO")


if __name__ == "__main__":
    main()
