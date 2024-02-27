for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)
    dp = [0] * len(a)
    for i in range(len(b)):
        if i == 0:
            dp[i] = b[0]
        else:
            dp[i] = dp[i - 1] + b[i]
    print(dp)
    indexes = []
    for i in range(len(a)):
        l = 0
        val = a[i]
        while l < len(dp) and val >= dp[l] - val:
            l += 1
        indexes.append(str(l))
    print(" ".join(indexes))
