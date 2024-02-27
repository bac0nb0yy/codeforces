x = list(input())

for i in range(len(x)):
    if i == 0 and x[i] == "9":
        continue
    if x[i] > "4":
        x[i] = str(9 - int(x[i]))
print("".join(x))
