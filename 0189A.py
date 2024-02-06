n, a, b, c = map(int, input().split())
p = sorted([a,b,c])
x = 0
s = 0
while s != n:
	s += p[0]