for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    bad_even = 0
    bad_odd = 0

    for i, e in enumerate(a):
        if i & 1 != e & 1:
            if i & 1:
                bad_odd += 1
            else:
                bad_even += 1

    print(-1 if bad_odd != bad_even else bad_even)
