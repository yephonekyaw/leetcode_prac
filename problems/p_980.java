public class p_980 {
    public static int find_path(int[][] grid, int row, int col, int covered_cells, int empty_cells) {
        if (grid[row][col] == 2) {
            return (covered_cells == empty_cells) ? 1 : 0;
        }

        int count = 0;
        if (row > 0) {
            if (grid[row - 1][col] == 0) {
                grid[row - 1][col] = 1;
                count += find_path(grid, row - 1, col, covered_cells + 1, empty_cells);
                grid[row - 1][col] = 0;
            } else if (grid[row - 1][col] == 2) {
                count += find_path(grid, row - 1, col, covered_cells + 1, empty_cells);
            }
        }
        if (row < grid.length - 1) {
            if (grid[row + 1][col] == 0) {
                grid[row + 1][col] = 1;
                count += find_path(grid, row + 1, col, covered_cells + 1, empty_cells);
                grid[row + 1][col] = 0;
            } else if (grid[row + 1][col] == 2) {
                count += find_path(grid, row + 1, col, covered_cells + 1, empty_cells);
            }
        }
        if (col > 0) {
            if (grid[row][col - 1] == 0) {
                grid[row][col - 1] = 1;
                count += find_path(grid, row, col - 1, covered_cells + 1, empty_cells);
                grid[row][col - 1] = 0;
            } else if (grid[row][col - 1] == 2) {
                count += find_path(grid, row, col - 1, covered_cells + 1, empty_cells);
            }
        }
        if (col < grid[0].length - 1) {
            if (grid[row][col + 1] == 0) {
                grid[row][col + 1] = 1;
                count += find_path(grid, row, col + 1, covered_cells + 1, empty_cells);
                grid[row][col + 1] = 0;
            } else if (grid[row][col + 1] == 2) {
                count += find_path(grid, row, col + 1, covered_cells + 1, empty_cells);
            }
        }
        return count;
    }

    public static int uniquePathsIII(int[][] grid) {
        // first count the number of empty cells so that
        // if we reach the destination, the used path covers all empty cells
        int empty_cells = 0;
        int start_i = 0, start_j = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] != -1) empty_cells++;
                if (grid[i][j] == 1) {
                    start_i = i; start_j = j;
                }
            }
        }
        return find_path(grid, start_i, start_j, 1, empty_cells);
    }
    public static void main(String[] args) {
        int[][] gird = {
            {1,0,0,0},
            {0,0,0,0},
            {0,0,0,2},
        };
        System.out.println(uniquePathsIII(gird));
    }
}
