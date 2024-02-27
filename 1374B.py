for _ in range(int(input())):
    n = int(input())
    cnt_2 = cnt_3 = 0
    while not n % 2:
        n //= 2
        cnt_2 += 1
    while not n % 3:
        n //= 3
        cnt_3 += 1
    print(-1 if cnt_2 > cnt_3 or n > 2 else (cnt_3 - cnt_2) + cnt_3)
