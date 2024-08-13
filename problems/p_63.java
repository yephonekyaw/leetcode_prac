public class p_63 {
    public static int uniquePathWithObstacles(int[][] obstacleGrid) {
        int row = obstacleGrid.length, col = obstacleGrid[0].length;
        if (obstacleGrid[0][0] == 1) return 0;

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (i == 0 && j == 0) {
                    obstacleGrid[0][0] = 1;
                    continue;
                }

                if (obstacleGrid[i][j] == 1) {
                    obstacleGrid[i][j] = 0;
                    continue;
                }
                if (i > 0) obstacleGrid[i][j] += obstacleGrid[i - 1][j];
                if (j > 0) obstacleGrid[i][j] += obstacleGrid[i][j - 1];
            }
        }
        return obstacleGrid[row - 1][col - 1];
    }
    public static void main(String[] args) {
        int[][] obstacleGrid = {
            {0, 1},
            {0, 0}
        };
        System.out.println(uniquePathWithObstacles(obstacleGrid));
    }
}
