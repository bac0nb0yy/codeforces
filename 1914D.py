def find_maxs(arr, n):
	indexes = []
	for i in range(n):
		maxi = 0
		maxi_index = 0
		for k in range(len(arr)):
			if k not in indexes and arr[k] > maxi:
				maxi = arr[k]
				maxi_index = k
		indexes.append(maxi_index)
	return indexes

for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	c = list(map(int, input().split()))

	sa = find_maxs(a, 3)
	sb = find_maxs(b, 3)
	sc = find_maxs(c, 3)

	s = 0
	print(sa,sb,sc)
	for i in range(3):
		for j in range(3):
			for k in range(3):
				if i != j and i != k and j != k:
					s = max(s, a[sa[i]] + b[sb[j]] + c[sc[k]])
	print(s)
