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
        n = ir()
        a = lmir()

        cur_mx = a[0]
        rez = 0
        for i in range(1, len(a)):
            if (a[i - 1] > 0) != (a[i] > 0):
                rez += cur_mx
                cur_mx = a[i]
            else:
                cur_mx = max(cur_mx, a[i])
        print(rez + cur_mx)


if __name__ == "__main__":
    main()
