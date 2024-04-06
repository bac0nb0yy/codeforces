for _ in range(int(input())):
    n = int(input())
    s = input()
    print(s.count("@") if "**" not in s else s[: s.index("**")].count("@"))
