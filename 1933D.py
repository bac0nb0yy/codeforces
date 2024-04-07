for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))

    if a[0] == a[1]:
        for i in range(2, len(a)):
            if a[i] % a[0] != 0:
                print("YES")
                break
        else:
            print("NO")
    else:
        print("YES")
