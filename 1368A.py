# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        a, b, n = mir()
        c = max(a, b)
        cnt = 0
        while c <= n:
            if a > b:
                c += b
                b = a
            else:
                c += a
                a = b
            cnt += 1
        print(cnt)


if __name__ == "__main__":
    main()
