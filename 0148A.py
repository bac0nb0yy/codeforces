*a, d = [int(input()) for i in range(5)]
print(sum([any(x % k == 0 for k in a) for x in range(1, d + 1)]))
