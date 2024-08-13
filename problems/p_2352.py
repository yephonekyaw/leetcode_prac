def equalPairs(grid):
    rows, cols = [''] * len(grid), [''] * len(grid)
    for i in range(len(grid)):
        for j in range(len(grid)):
            rows[i] = ' '.join([rows[i], str(grid[i][j])])
            cols[j] = ' '.join([cols[j], str(grid[i][j])])

    col_freq = {col: cols.count(col) for col in cols}
    count = 0
    for row in rows:
        count += col_freq.get(row, 0)
    return count


def main():
    grid = [[13, 13], [13, 13]]
    print(equalPairs(grid))


main()
