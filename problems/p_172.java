public class p_172 {
    static int trailingZeroes(int n) {
        int num_of_zeros = 0;
        for (int i = 1; i <= 10; i++) {
            num_of_zeros += (n / (int)Math.pow(5, i));
        }

        return num_of_zeros;
    }

    public static void main(String[] args) {
        int n = 625;
        System.out.println(trailingZeroes(n));
    }


}
