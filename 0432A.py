n, k = map(int, input().split())
y = [i for i in map(int, input().split()) if i + k <= 5]
print(len(y)//3)