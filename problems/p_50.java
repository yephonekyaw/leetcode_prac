/**
 * p_50
 */
public class p_50 {
    static double myPow(double x, int n) {
        if (n == -1) {
            return 1 / x;
        } else if (n == 1) {
            return x;
        }

        if (n < -1) {
            return (1 / x) * myPow(x, n + 1);
        }

        return x * myPow(x, n - 1);
    }

    public static void main(String[] args) {
        double x = 2.00000;
        int n = -2;
        System.out.printf("%.5f", myPow(x, n));
    }
}