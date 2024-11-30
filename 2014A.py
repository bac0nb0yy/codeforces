for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    money = 0
    count = 0
    for i in a:
        if i >= k:
            money += i
        elif i == 0 and money > 0:
            money -= 1
            count += 1
    print(count)
