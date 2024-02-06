from functools import cache
import sys


def get_parents(node, parent):
    parents[node] = parent
    for neighbor in tree[node]:
        if neighbor != parent:
            get_parents(neighbor, node)


@cache
def count_offspring(node, parent):
    rez = 0
    for neighbor in tree[node]:
        if neighbor != parent:
            rez += 1 + count_offspring(neighbor, node)
    return rez


n, k = map(int, sys.stdin.readline().split())
tree = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    u -= 1
    v -= 1
    tree[u].append(v)
    tree[v].append(u)
parents = [None] * n
get_parents(0, None)
offspring = [count_offspring(node, parents[node]) for node in range(n)]
is_touristic = [False] * n
offspring = sorted([(o, i) for i, o in enumerate(offspring)], reverse=True)
for i in range(n - k):
    is_touristic[offspring[i][1]] = True

l=3
print(is_touristic)
