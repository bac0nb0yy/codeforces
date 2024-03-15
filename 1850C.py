for _ in range(int(input())):
    rez = ""
    for _ in range(8):
        row = input()
        for i in range(len(row)):
            if row[i] != ".":
                rez += row[i]
                break
    print(rez)
