n = int(input())

all_cubes = 1
line = 1
counter = 1
while all_cubes <= n:
    line = line + (counter + 1)
    all_cubes += line
    counter += 1
print(counter if all_cubes <= n else counter - 1)
