# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    n = ir()
    s = input()
    h = set()
    two_grams = []
    for i in range(1, len(s)):
        d = s[i - 1] + s[i]
        if d not in h:
            two_grams.append([s.count(d), d])
            h.add(d)
    print(max(two_grams)[1])


if __name__ == "__main__":
    main()
