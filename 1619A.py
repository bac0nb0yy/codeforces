for _ in range(int(input())):
    s = input()
    print("YES" if not len(s) & 1 and s[: len(s) // 2] == s[len(s) // 2 :] else "NO")
