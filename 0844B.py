def count_col(grid, x, target, rows):
    occ = 0
    for row in range(rows):
        if grid[row][x] == target:
            occ += 1
    return occ


n, m = map(int, input().split())

grid = []
sets = 0
for row in range(n):
    grid.append(list(map(int, input().split())))

for row in range(n):
    occ_zero = grid[row].count(0)
    occ_one = grid[row].count(1)
    sets += 2**occ_zero - occ_zero - 1
    sets += 2**occ_one - occ_one - 1

for col in range(m):
    occ_zero = count_col(grid, col, 0, n)
    occ_one = count_col(grid, col, 1, n)
    sets += 2**occ_zero - occ_zero - 1
    sets += 2**occ_one - occ_one - 1

print(sets + n * m)
