for _ in range(int(input())):
    n = int(input())
    grid = []
    index = 0
    for i in range(n):
        row = input()
        if "1" in row:
            index = i
        grid.append(row)
    print(
        "SQUARE" if grid[index].count("1") == grid[index - 1].count("1") else "TRIANGLE"
    )
