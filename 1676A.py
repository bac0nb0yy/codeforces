for _ in range(int(input())):
    s = input()
    first = s[:3]
    last = s[3:]
    if sum(int(i) for i in first) == sum(int(i) for i in last):
        print("YES")
    else:
        print("NO")