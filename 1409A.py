t = int(input())
for _ in range(t):
	a, b = map(int, input().split())
	diff = abs(a - b)
	print(diff // 10 + (diff % 10 != 0))