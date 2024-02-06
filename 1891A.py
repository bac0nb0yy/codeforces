t = int(input())
for _ in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	m = True
	for i in range(1, len(a)):
		if a[i] - a[i - 1] < 0 and not ((i & (i-1) == 0) and i != 0):
			m = False
			break
	print(["NO","YES"][m])