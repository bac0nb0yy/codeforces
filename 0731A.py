s = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"

count = 0
start = 0
for i in s:
    count += min(abs(alphabet.index(i) - start), 26 - abs(alphabet.index(i) - start))
    start = alphabet.index(i)
print(count)
