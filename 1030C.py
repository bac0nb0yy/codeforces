n = int(input())
a = input()

first = 0
for i in range(len(a)):
    first += int(a[i])
    second = -1
    find = True
    pos = i + 1
    while pos < n:
        second = int(a[pos])
        pos += 1
        while pos < n and second + int(a[pos]) <= first:
            second += int(a[pos])
            pos += 1
        if first != second:
            find = False
            break
    if first != second:
        find = False
    if find:
        print("YES")
        break
else:
    print("NO")
