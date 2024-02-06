n = int(input())
a = list(map(int, input().split()))


def check_not_even(a):
    count = 0
    index = 0
    for i in range(len(a)):
        if a[i] % 2:
            count += 1
            if count > 1:
                return (0, 0)
            index = i
    return (count, index)


def first_even(a):
    for i in range(len(a)):
        if a[i] % 2 == 0:
            return i


check = 1
fail = 0
index = 0
if check_not_even(a)[0] == 0:
    print(first_even(a) + 1)
else:
    print(check_not_even(a)[1] + 1)
