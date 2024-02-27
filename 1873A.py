import copy

for _ in range(int(input())):
    l = list(input())
    if l == ["a", "b", "c"]:
        print("YES")
        continue
    find = False
    for i in range(3):
        for k in range(3):
            if i != k:
                tmp = copy.deepcopy(l)
                tmp[i], tmp[k] = tmp[k], tmp[i]
                if tmp == ["a", "b", "c"]:
                    find = True
                    break
    print("YES" if find else "NO")
