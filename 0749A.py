n = int(input())

po = n >> 1

print(po)
if n & 1:
    print("2 " * (po - 1) + "3")
else:
    print(" ".join(["2" for i in range(po)]))
