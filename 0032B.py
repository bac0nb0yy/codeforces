s = input()
rez = []
i = 0
while i < len(s):
    if s[i] == ".":
        rez += ["0"]
    elif s[i] == "-":
        if s[i + 1] == ".":
            rez += ["1"]
        else:
            rez += ["2"]
        i += 1
    i += 1
print("".join(rez))