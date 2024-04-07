from collections import defaultdict


for _ in range(int(input())):
    s = input()

    rez = defaultdict(bool)
    i = 0
    while i < len(s):
        j = i
        while j + 1 < len(s) and s[j + 1] == s[i]:
            j += 1
        if not (j - i) & 1:
            rez[s[i]] = True
        i = j + 1
    good = ""
    for c in "abcdefghijklmnopqrstuvwxyz":
        if rez[c]:
            good += c
    print(good)
