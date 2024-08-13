/**
 * p_29
 */

/*
 * Divide two numbers by using bit manipulation
 * For example: 97 / 7 is (7 * 13) + 6, we don't really care about the remainder part in this problem
 * So, let's stop and think for a moment about how we can rewrite this (7 * 13)
 * It turns out that we can write any numbers by using the binary. 13 is 2^3 + 2^2 + 2^0. Therefore,
 * (7 * 13) can be rewritten as (7 * 2^3) + (7 * 2^2) + (7 * 2^0).
 * We now know the pattern, so the question is how can we implement this idea as an algorithm.
 * 
 * We are going to use the bitwise operation, particularly left shift bit manipulation.
 * What left-shifting does is that it multiplies the number in front by 2 to the power of shifted bits.
 * For instance, 7 << 2 is 28 because 7 is multiplied by 2 to the power of 2, which is 4.
 * In each iteration, we are going to look for the largest power of 2 to multiply the divisor, but the result
 * must be less than the dividend itself.
 * For example, in the case of (97 / 7), (7 * 2^3), (7 * 2^2), (7 * 2^0) are all acceptable, however, we are going to choose
 * the largest power in the first iteration, which is 3. Then the second largest power in second iteration, which is 2, and
 * the power of 0 in the last iteration.
 */
public class p_29 {
    public static int divide(int dividend, int divisor) {
        if (dividend == Integer.MAX_VALUE && divisor == -1) {
            return Integer.MAX_VALUE;
        }

        int quotient = 0;
        boolean minus_flag = false;

        if (dividend < 0 && divisor < 0) minus_flag = false;
        else if (dividend < 0 || divisor < 0) minus_flag = true;
        dividend = (int)Math.abs(dividend);
        divisor = (int)Math.abs(divisor);

        while (dividend - divisor >= 0) {
            int power = 0;
            while (dividend - (divisor << (power + 1)) >= 0) {
                power++;
            }
            dividend -= (divisor << power);
            quotient += (1 << power);
        }   

        return (minus_flag) ? -1 * quotient : quotient;
    }

    public static void main(String[] args) {
        int dividend = 1;
        int divisor = 1;
        System.out.println(divide(dividend, divisor));
        System.out.println(Integer.MIN_VALUE);
    }
}