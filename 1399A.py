t = int(input())
for _ in range(t):
	n = int(input())
	a = sorted(list(map(int, input().split())))
	y = True
	for i in range(1, len(a)):
		if a[i] != a[i - 1] and a[i] - 1 != a[i - 1]:
			y = False
			break
	print("YES" if y else "NO")