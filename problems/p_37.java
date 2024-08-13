import java.util.*;

public class p_37 {
    public static boolean checkRow(char[][] board, int row, int col, int num) {
        for (int j = 0; j < 9; j++) {
            if (j == col) continue;
            if (board[row][j] - '0' == num) return false;
        }
        return true;
    }

    public static boolean checkCol(char[][] board, int row, int col, int num) {
        for (int i = 0; i < 9; i++) {
            if (i == row) continue;
            if (board[i][col] - '0' == num) return false;
        }
        return true;
    }

    public static boolean checkBlock(char[][] board, int row, int col, int num) {
        for (int i = (row / 3) * 3; i < (row / 3) * 3 + 3; i++) {
            for (int j = (col / 3) * 3; j < (col/ 3) * 3 + 3; j++) {
                if (i == row && j == col) continue;
                if (board[i][j] - '0' == num) return false;
            }
        }
        return true;
    }

    public static int[] findEmptyCell(char[][] board) {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') return new int[]{i, j};
            }
        }
        return new int[]{-1, -1};
    }

    public static boolean solve(char[][] board) {
        int[] free_cell = findEmptyCell(board);
        int row = free_cell[0], col = free_cell[1];
        if (row == -1 && col == -1) return true;
        
        for (int i = 1; i <= 9; i++) {
            if (checkRow(board, row, col, i) && checkCol(board, row, col, i) && checkBlock(board, row, col, i)) {
                board[row][col] = (char)(i + '0');
                if (solve(board)) return true;
                board[row][col] = '.';
            }
        }
        return false;
    }

    public static void solveSudoku(char[][] board) {
        System.out.println(solve(board));
    }

    public static void main(String[] args) {
        char[][] board = {
            {'5', '3', '.', '.', '7', '.', '.', '.', '.'},
            {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
            {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
            {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
            {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
            {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
            {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
            {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
            {'.', '.', '.', '.', '8', '.', '.', '7', '9'},
        };
        solveSudoku(board);
        System.out.println(Arrays.deepToString(board));
    }
}
