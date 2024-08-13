public class p_59 {
    public static int[][] generateMatrix(int n) {
        int[][] matrix = new int[n][n];
        int count = 1;
        int rep = 0;
        while(true) {
            int row = rep;
            int col = rep;

            // go left
            while (col < n - rep) {
                matrix[row][col] = count;
                count++;
                col++;
            }
            if (count == n * n + 1) break;
            
            // go down
            row++;
            col--;
            while (row < n - rep) {
                matrix[row][col] = count;
                count++;
                row++;
            }
            if (count == n * n + 1) break;

            // go right
            row--;
            col--;
            while (col > rep - 1) {
                matrix[row][col] = count;
                count++;
                col--;
            }
            if (count == n * n + 1) break;

            // go up
            row--;
            col++;
            while (row > rep) {
                matrix[row][col] = count;
                count++;
                row--;
            }
            if (count == n * n + 1) break;
            rep++;
        }

        return matrix;
    }

    public static void main(String[] args) {
        int[][] matrix = generateMatrix(3);
        for (int[] arr: matrix) {
            for (int num: arr) {
                System.out.print(num + " ");
            }
        }
    }
}
