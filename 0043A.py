from collections import defaultdict

w = defaultdict(int)
for i in range(int(input())):
    w[input()] += 1
print(max(w.items(), key=lambda x: x[1])[0])
