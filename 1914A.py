for _ in range(int(input())):
	n = int(input())
	s = sorted(input())
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	l = dict()
	c = 0
	for i in s:
		if s.count(i) > alphabet.index(i) and i not in l:
			c += 1
			l[i] = True
	print(c)