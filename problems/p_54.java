import java.util.*;

public class p_54 {
    static boolean checkFull(List<Integer> spiral, int[][] matrix) {
        return spiral.size() == (matrix.length * matrix[0].length);
    }

    static List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> spiral = new ArrayList<>();
        int rep = 0;
        int size = matrix.length;
        while (rep <= size / 2) {
            int row = rep;
            int col = rep;

            // go left
            while (col < matrix[0].length - rep) {
                spiral.add(matrix[row][col]);
                col++;
            }
            if(checkFull(spiral, matrix)) break;

            // go down
            row++;
            col--;
            while (row < matrix.length - rep) {
                spiral.add(matrix[row][col]);
                row++;
            }
            if (checkFull(spiral, matrix)) break;

            // go right
            row--;
            col--;
            while (col > rep - 1) {
                spiral.add(matrix[row][col]);
                col--;
            }
            if (checkFull(spiral, matrix)) break;
            
            // go up
            row--;
            col++;
            while (row > rep) {
                spiral.add(matrix[row][col]);
                row--;
            }
            if (checkFull(spiral, matrix)) break;

            rep++;
        }

        return spiral;
    }
    public static void main(String[] args) {
        int[][] matrix = {
            {1, 2, 3, 4},
            {5, 6, 7, 8},
            {9, 10, 11, 12}
        };
        List<Integer> spiral = spiralOrder(matrix);
        for (int num: spiral) {
            System.out.print(num + " ");
        }
    }
}
