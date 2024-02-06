n = int(input())
c = 0
while n:
	c += n & 1
	n >>= 1
print(c)