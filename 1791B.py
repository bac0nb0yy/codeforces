for _ in range(int(input())):
    n = int(input())
    s = input()
    good = False
    pos = [0, 0]
    for direction in s:
        if direction == "L":
            pos[0] -= 1
        elif direction == "R":
            pos[0] += 1
        elif direction == "U":
            pos[1] += 1
        else:
            pos[1] -= 1
        if pos == [1, 1]:
            good = True
            break
    print("YES" if good else "NO")
