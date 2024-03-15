n, k = map(int, input().split())
a = list(map(int, input().split()))
t = list(map(int, input().split()))

dp_yes = [0] * (n)
dp_no = [0] * (n)

for i in range(n):
    dp_yes[i] = dp_yes[i - 1] + a[i]
    dp_no[i] = dp_no[i - 1] + a[i] * t[i]

maxi = dp_no[-1]

for i in range(n - k + 1):
    maxi = max(
        maxi,
        (
            dp_no[i - 1] + (dp_yes[i + k - 1] - dp_yes[i - 1])
            if i > 0
            else dp_yes[i + k - 1]
        )
        + (dp_no[-1] - dp_no[i + k - 1]),
    )

print(maxi)
