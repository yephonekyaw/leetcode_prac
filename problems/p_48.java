public class p_48 {
    static void rotate(int[][] matrix) {
        // 0,0 - 0,3 - 3,3 - 3,0 - 0,0
        // 0,1 - 1,3 - 3,2 - 2,0 - 0,1
        // 0,2 - 2,3 - 3,1 - 1,0 - 0,2

        int size = matrix.length;
        int times = size / 2;
        int row = 0;
        while (row < times) {
            for (int j = row; j < (size - row - 1); j++) {

                // up to last
                int replacer = matrix[row][j];
                int replaced = matrix[j][size - row - 1];
                matrix[j][size - row - 1] = replacer;

                // last to down
                replacer = replaced;
                replaced = matrix[size - row - 1][size - j - 1];
                matrix[size - row - 1][size - j - 1] = replacer;

                // down to first
                replacer = replaced;
                replaced = matrix[size - j - 1][row];
                matrix[size - j - 1][row] = replacer;

                // first to up
                replacer = replaced;
                matrix[row][j] = replacer;
            }
            row++;
        }
    }

    public static void main(String[] args) {
        int[][] matrix = {
            {5, 1, 9, 11},
            {2, 4, 8, 10},
            {13, 3, 6, 7},
            {15, 14, 12, 16}
        };
        rotate(matrix);
        for (int[] arr: matrix) {
            for (int num: arr) {
                System.out.print(num + " ");
            }
            System.out.println();
        }
    }
}
