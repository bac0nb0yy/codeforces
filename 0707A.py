n, m = map(int, input().split())
color = False
for _ in range(n):
    row = input().split()
    if "C" in row or "M" in row or "Y" in row:
        color = True
print("#Color" if color else "#Black&White")
