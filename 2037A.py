from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for k, v in Counter(a).items():
        cnt += v // 2
    print(cnt)
