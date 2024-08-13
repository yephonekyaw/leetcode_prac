public class p_36 {
    static boolean checkRow(char[][] borad, int row, int col) {
        for (int i = 0; i < 9; i++) {
            if (i != row && borad[row][col] == borad[i][col]) return false;
        }
        return true;
    }

    static boolean checkCol(char[][] borad, int row, int col) {
        for (int j = 0; j < 9; j++) {
            if (j != col && borad[row][col] == borad[row][j]) return false;
        }
        return true;
    }

    static boolean checkBox(char[][] borad, int row, int col) {
        int start_row = (row / 3) * 3;
        int start_col = (col / 3) * 3;
        for (int i = start_row; i < (start_row + 3); i++) {
            for (int j = start_col; j < (start_col + 3); j++) {
                if (i == row && j == col) continue;
                if (borad[row][col] == borad[i][j]) return false;
            }
        }
        return true;
    }

    static boolean isValidSudoku(char[][] board) {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.') {
                    if (checkRow(board, i, j) && checkCol(board, i, j) && checkBox(board, i, j)) {
                        continue;
                    } else {
                        return false;
                    }
                }
            }
        }
        return true;
    }

    public static void main(String[] args) {
        char[][] board = {
            {'.', '.', '4', '.', '.', '.', '6', '3', '.'},
            {'.', '.', '.', '.', '.', '.', '.', '.', '.'},
            {'5', '.', '.', '.', '.', '.', '.', '9', '.'},
            {'.', '.', '.', '5', '6', '.', '.', '.', '.'},
            {'4', '.', '3', '.', '.', '.', '.', '.', '1'},
            {'.', '.', '.', '7', '.', '.', '.', '.', '.'},
            {'.', '.', '.', '5', '.', '.', '.', '.', '.'},
            {'.', '.', '.', '.', '.', '.', '.', '.', '.'},
            {'.', '.', '.', '.', '.', '.', '.', '.', '.'},
        };
        System.out.println(isValidSudoku(board));
    }
}