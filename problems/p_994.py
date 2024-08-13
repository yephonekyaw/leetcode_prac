from collections import deque

def orangesRotting(grid):
    """
        2 1 1
        0 1 1
        1 0 1
    """
    about_rotten = deque()
    fresh_ones = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                about_rotten.append([i, j])
            elif grid[i][j] == 1:
                fresh_ones += 1
    
    # zero minute is required to spoil the field
    if fresh_ones == 0:
        return 0

    required_min = 0
    row_end, col_end = len(grid) - 1, len(grid[0]) - 1
    while about_rotten:
        rotten = about_rotten
        about_rotten = deque()
        while rotten:
            x, y = rotten.popleft()
            if x > 0 and grid[x - 1][y] == 1:
                about_rotten.append([x - 1, y])
                grid[x - 1][y] = 2
                fresh_ones -= 1
            if x < row_end and grid[x + 1][y] == 1:
                about_rotten.append([x + 1, y])
                grid[x + 1][y] = 2
                fresh_ones -= 1
            if y > 0 and grid[x][y - 1] == 1:
                about_rotten.append([x, y - 1])
                grid[x][y - 1] = 2
                fresh_ones -= 1
            if y < col_end and grid[x][y + 1] == 1:
                about_rotten.append([x, y + 1])
                grid[x][y + 1] = 2
                fresh_ones -= 1
        required_min += 1
    
    return required_min - 1 if fresh_ones == 0 else -1


def main():
    grid = [[0,2]]
    print(orangesRotting(grid))

main()