from collections import deque
import sys


for _ in range(int(input())):
    n = int(input())
    s = list(input())
    queue = deque([s])
    best = sys.maxsize
    while queue:
        seq = queue.popleft()
        new = []
        i = 0
        while i < len(seq):
            if seq[i] == "(" and i < len(seq) - 1 and seq[i + 1] == ")":
                i += 2
            else:
                new.append(seq[i])
                i += 1
        best = min(best, len(new) // 2)
        if new != seq:
            queue.append(new)
    print(best)
