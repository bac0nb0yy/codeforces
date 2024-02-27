from collections import Counter

good_counter = Counter("Timur")

for _ in range(int(input())):
    n = int(input())
    s = input()
    print("YES" if Counter(s) == good_counter else "NO")
