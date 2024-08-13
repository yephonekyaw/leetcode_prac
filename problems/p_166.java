import java.util.*;

public class p_166 {
    static String fractionToDecimal(int numerator, int denominator) {
        Map<Long, Long> remainders = new LinkedHashMap<>();
        long count = 0;
        long key = -1L;
        int sign = 1;
        String res = "";

        if (numerator == 0) return "0";

        if (denominator != 0) {
            sign *= ((numerator < 0) ? -1 : 1) * ((denominator < 0) ? -1 : 1);
            long nume = (numerator == Integer.MIN_VALUE) ? 
                        2147483648L : 
                        Math.abs(numerator);
            long deno = (denominator == Integer.MIN_VALUE) ?
                        2147483648L :
                        Math.abs(denominator);
            long quotient = nume / deno;

            long remainder = (nume % deno) * 10;
            while (count < deno && key == -1 && remainder != 0) {
                if (remainders.containsKey(remainder)) {
                    key = remainder;
                    break;
                }

                remainders.put(remainder, remainder / deno);
                remainder = (remainder % deno) * 10;
                count++;
            }
        
            res += quotient + ((remainders.size() == 0) ? "" : ".");
            for (long k: remainders.keySet()) {
                if (k == key) res += "(";
                res += remainders.get(k);
            }
            System.out.println(quotient);
            return ((sign == -1) ? "-" : "") + res + ((key == -1) ? "" : ")");
        }
        return res;
    }
    public static void main(String[] args) {
        int numerator = -50;
        int denominator = 8;
        System.out.println(fractionToDecimal(numerator, denominator));
    }
}
