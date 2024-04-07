import sys

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    prefix = [0] * (n)
    prefix[n - 1] = b[n - 1]
    for i in reversed(range(n - 1)):
        prefix[i] = prefix[i + 1] + b[i]

    dp_yes = [sys.maxsize] * (n)
    dp_no = [sys.maxsize] * (n)
    dp_yes[n - 1] = a[n - 1]
    for i in reversed(range(n - 1)):
        dp_yes[i] = min(min(dp_yes[i + 1], dp_no[i + 1]) + a[i], a[i] + prefix[i + 1])
        dp_no[i] = min(dp_yes[i + 1], dp_no[i + 1]) + b[i]
    print(min(dp_yes[:m]))
