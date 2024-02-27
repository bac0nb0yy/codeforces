for _ in range(int(input())):
    n = int(input())
    s = sorted(list(map(int, input().split())))
    mini = s[1] - s[0]
    for i in range(2, len(s)):
        mini = min(mini, s[i] - s[i - 1])
    print(mini)
