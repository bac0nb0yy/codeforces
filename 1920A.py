import sys

for _ in range(int(input())):
    n = int(input())
    gt = -sys.maxsize
    lt = sys.maxsize
    diff = set()
    for _ in range(n):
        a, x = map(int, input().split())
        if a == 1:
            gt = max(gt, x)
        elif a == 2:
            lt = min(lt, x)
        else:
            diff.add(x)
    print(max(0, ((lt + 1) - gt) - sum(gt <= i <= lt for i in diff)))
