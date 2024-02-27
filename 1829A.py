GOOD = "codeforces"

for _ in range(int(input())):
    s = input()
    print(sum(s[i] != GOOD[i] for i in range(len(s))))
