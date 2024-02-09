from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    s = input()
    visited = defaultdict(bool)
    i = 0
    sus = False
    while i < len(s):
        if visited[s[i]]:
            sus = True
            break
        visited[s[i]] = True
        val = s[i]
        while i < len(s) and s[i] == val:
            i += 1
    print("YES" if not sus else "NO")
