for _ in range(int(input())):
    n = int(input())
    s = input()
    print(len(set(s)) * 2 + sum(s.count(i) - 1 for i in set(s)))
