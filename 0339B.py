n, m = map(int, input().split())
a = list(map(int, input().split()))
prev = a[0]
o = prev - 1
for i in a[1:]:
	if i < prev:
		o += ((n - prev) + i)
	else:
		o += (i - prev)
	prev = i
print(o)