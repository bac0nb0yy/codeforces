from collections import deque


def bfs(queue, n):
    players = set()
    while queue:
        i, r, c = queue.popleft()
        if "0" in c:
            position = (i + r) % n
            players.add(position if position != 0 else n)
        if "1" in c:
            position = (i - r) % n
            players.add(position if position != 0 else n)

    return players


for _ in range(int(input())):
    n, m, x = map(int, input().split())
    goods = [x]
    for i in range(m):
        r, c = input().split()
        r = int(r)
        c = c.replace("?", "01")
        queue = deque()
        for i in goods:
            queue.append([i, r, c])
        goods = bfs(queue, n)
    print(len(goods))
    print(*sorted(goods))
