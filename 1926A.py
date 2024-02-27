from collections import Counter

for _ in range(int(input())):
    c = Counter(input())
    print("A" if c["A"] > c["B"] else "B")
