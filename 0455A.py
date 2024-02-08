from collections import Counter

n = int(input())
a = list(map(int, input().split()))
c = Counter(a)

dp_yes = [0, 0]
dp_no = [0, 0]
prev = -1
for k, v in sorted(c.items()):
    dp_yes.append(k * v + max(dp_yes[-1] if prev + 1 != k else dp_yes[-2], dp_no[-1]))
    dp_no.append(max(dp_yes[-2], dp_no[-1]))
    prev = k

print(max(dp_yes[-1], dp_no[-1]))
