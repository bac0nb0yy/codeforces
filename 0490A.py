from collections import Counter
from collections import defaultdict

n = int(input())
t = list(map(int, input().split()))

w = min(t.count(1), t.count(2), t.count(3))
print(w)
s = defaultdict(list)
for i, e in enumerate(t):
    s[e] += [i + 1]
for i in range(w):
    print(s[1][i], s[2][i], s[3][i])