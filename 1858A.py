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
    for _ in rir():
        a, b, c = mir()
        if a + math.ceil(c / 2) > b + math.floor(c / 2):
            print("First")
        else:
            print("Second")


if __name__ == "__main__":
    main()
