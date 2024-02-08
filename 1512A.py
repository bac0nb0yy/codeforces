from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    for k,v in Counter(a).items():
        if v == 1:
            print(a.index(k) + 1)
            break