for _ in range(int(input())):
    n = int(input())
    s = input()
    l, r = 0, n - 1
    while l < r and ((s[l] == "0" and s[r] == "1") or (s[l] == "1" and s[r] == "0")):
        l += 1
        r -= 1
    print(n - (l * 2))
