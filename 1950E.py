import math


def find_divisors(n):
    divisors = set()
    for i in range(1, math.isqrt(n) + 1):
        if not n % i:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(list(divisors))


def check_repeating_substring(s, length):
    sub = s[:length]
    count = 0
    for j in range(len(s)):
        if s[j] != sub[j % len(sub)]:
            count += 1
            if count > 1:
                break
    if count < 2:
        return True
    sub = s[length : length * 2]
    count = 0
    for j in range(len(s)):
        if s[j] != sub[j % len(sub)]:
            count += 1
            if count > 1:
                break
    if count < 2:
        return True
    return False


for _ in range(int(input())):
    n = int(input())
    s = input()
    divisors = find_divisors(n)
    for i in divisors:
        if check_repeating_substring(s, i):
            print(i)
            break
