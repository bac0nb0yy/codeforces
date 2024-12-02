# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    k = ir()
    a = sorted(lmir(), reverse=True)
    cnt = 0
    taken = 0
    for i in a:
        if cnt >= k:
            break
        cnt += i
        taken += 1
    print(taken if cnt >= k else -1)


if __name__ == "__main__":
    main()
