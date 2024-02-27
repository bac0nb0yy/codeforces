for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    hashmap = set()
    rez = "YES"
    for i in a:
        if i in hashmap:
            rez = "NO"
            break
        hashmap.add(i)
    print(rez)
