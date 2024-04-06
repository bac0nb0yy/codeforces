import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    counter = [0] * (n + 1)
    for i in a:
        if counter[i] == 2:
            print(i)
            break
        counter[i] += 1
    else:
        print(-1)
