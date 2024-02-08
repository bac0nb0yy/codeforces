n = int(input())
a = list(map(int, input().split()))
maxi = max(a)
print(sum(maxi - i for i in a))