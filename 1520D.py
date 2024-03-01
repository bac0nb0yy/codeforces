from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = defaultdict(int)
    count = 0
    for i in range(n):
        count += s[a[i] - i]
        s[a[i] - i] += 1
    print(count)
