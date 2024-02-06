for _ in range(int(input())):
	n, k = map(int, input().split())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	s = 0
	curr_quest = 0
	for i in range(k):
		print(s, curr_quest)
		if i >= len(b):
			s += sum(b)
			continue
		elif i == 0:
			s += a[0]
			curr_quest += 1
			continue
		elif i == k - 1:
			if sum(b[:i]) <= b[i]:
				curr_quest += 1
				s += a[i]
				continue
		else:
			curr_quest += 1
			s += a[i]
		s += sum(b[:curr_quest])
	print()
	print(s)