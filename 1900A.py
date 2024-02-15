for _ in range(int(input())):
    n = int(input())
    s = input()
    best = cur = 0
    for i in range(len(s)):
        if s[i] == ".":
            cur += 1
            best = max(best, cur)
            if best == 3:
                break
        else:
            cur = 0
    print("2" if best == 3 else s.count("."))
