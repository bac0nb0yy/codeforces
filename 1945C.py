from collections import deque, defaultdict
import sys

for _ in range(int(input())):
    n = int(input())
    a = input()

    ones = sum(i == "1" for i in a)
    zeros = n - ones
    middle = n // 2
    right = sum(i == "1" for i in a[:middle])
    left = sum(i == "0" for i in a[:middle])

    queue = deque([[middle, left, right]])
    visited = defaultdict(bool)
    rez = []
    while queue:
        pos, l, r = queue.popleft()
        if l >= r and (ones - r) >= (zeros - l):
            rez.append(pos)
        visited[pos] = True
        if pos - 1 >= 0 and not visited[pos - 1]:
            queue.append(
                [
                    pos - 1,
                    l - (a[pos - 1] == "0"),
                    r - (a[pos - 1] == "1"),
                ]
            )
            visited[pos - 1] = True
        if pos + 1 <= n and not visited[pos + 1]:
            queue.append([pos + 1, l + (a[pos] == "0"), r + (a[pos] == "1")])
            visited[pos + 1] = True
    rez = sorted(rez)
    diff = sys.maxsize
    pos = -1
    for i in range(len(rez)):
        if abs((n / 2) - rez[i]) < diff:
            diff = abs(rez[i] - n // 2)
            pos = i
    print(rez[pos])
