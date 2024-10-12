for _ in range(int(input())):
    s = input()
    if len(s) == s.count(s[0]):
        print("NO")
    else:
        diff = 0
        for i in range(1, len(s)):
            if s[i] != s[0]:
                diff = i
                break
        s = list(s)
        s[0], s[diff] = s[diff], s[0]
        print("YES")
        print("".join(s))
