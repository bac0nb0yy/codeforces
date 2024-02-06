from collections import Counter

n = int(input())
s = list(map(int, input().split()))
c = Counter(s)
ans = c[4]
m = min(c[1], c[3])
ans += m
c[1] -= m
c[3] -= m
ans += c[3]
ans += c[2] >> 1
if c[2] & 1:
    ans += 1
    c[1] = max(0, c[1] - 2)
ans += (c[1] + 3) // 4
print(ans)
