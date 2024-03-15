import itertools

h, w = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(h)]
sets = 0
for line in itertools.chain(grid, zip(*grid)):
    occ_zero = line.count(0)
    occ_one = len(line) - occ_zero
    sets += (1 << occ_zero) + (1 << occ_one)
print(sets - h * w - 2 * (h + w))
