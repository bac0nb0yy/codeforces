direction = input()
seq = input()

layout = "qwertyuiopasdfghjkl;zxcvbnm,./"

if direction == "L":
    print("".join([layout[layout.index(i) + 1] for i in seq]))
else:
    print("".join([layout[layout.index(i) - 1] for i in seq]))
