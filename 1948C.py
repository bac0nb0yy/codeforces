from collections import deque, defaultdict

for _ in range(int(input())):
    n = int(input())
    grid = [input(), input()]

    def isAccessible(x, y, n):
        return (0 <= x < n) and (0 <= y < 2)

    def nextPos(x, y):
        if grid[y][x] == ">":
            return [x + 1, y]
        return [x - 1, y]

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque([[0, 0]])
    visited = defaultdict(bool)
    end = False
    while queue:
        x, y = queue.popleft()
        if x == n - 1 and y == 1:
            end = True
            break
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if isAccessible(nx, ny, n) and not visited[nx, ny]:
                nxx, nyy = nextPos(nx, ny)
                if not visited[nxx, nyy]:
                    queue.append([nxx, nyy])
                    visited[nx, ny] = True
                    visited[nxx, nyy] = True
    print("YES" if end else "NO")
