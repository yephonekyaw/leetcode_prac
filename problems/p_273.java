import java.util.*;

public class p_273 {

    static HashMap<Integer, String> initialize_mappings() {
        HashMap<Integer, String> mappings = new HashMap<>();
        mappings.put(0, "");
        mappings.put(1, "One ");
        mappings.put(2, "Two ");
        mappings.put(3, "Three ");
        mappings.put(4, "Four ");
        mappings.put(5, "Five ");
        mappings.put(6, "Six ");
        mappings.put(7, "Seven ");
        mappings.put(8, "Eight ");
        mappings.put(9, "Nine ");
        mappings.put(10, "Ten ");
        mappings.put(11, "Eleven ");
        mappings.put(12, "Twelve ");
        mappings.put(13, "Thirteen ");
        mappings.put(14, "Fourteen ");
        mappings.put(15, "Fifteen ");
        mappings.put(16, "Sixteen ");
        mappings.put(17, "Seventeen ");
        mappings.put(18, "Eighteen ");
        mappings.put(19, "Nineteen ");
        mappings.put(20, "Twenty ");
        mappings.put(30, "Thirty ");
        mappings.put(40, "Forty ");
        mappings.put(50, "Fifty ");
        mappings.put(60, "Sixty ");
        mappings.put(70, "Seventy ");
        mappings.put(80, "Eighty ");
        mappings.put(90, "Ninety ");
        mappings.put(100, "Hundred ");
        mappings.put(1000, "Thousand ");
        mappings.put(1000000, "Million ");
        mappings.put(1000000000, "Billion ");

        return mappings;
    }

    static String operation_on_three(int number, HashMap<Integer, String> mappings, int mult) {
        if (number == 0) return "";

        int quotient = number / (int)Math.pow(10, mult);

        // if 3 digit, we have to retrieve Hundred as well
        if (mult == 2 && quotient != 0) {
            return mappings.get(quotient) +
                   mappings.get(100) +
                   operation_on_three(number % (int)Math.pow(10, mult), mappings, mult - 1);
        }

        // ten edge cases 10 - 19
        if (number >= 10 && number <= 19) {
            return mappings.get(number);
        }

        // 2 digit and 1 digit
        return mappings.get(quotient * (int)Math.pow(10, mult)) +
               operation_on_three(number % (int)Math.pow(10, mult), mappings, mult - 1);
    }

    static String numberToWords(int num) {
        if (num == 0) return "Zero";

        HashMap<Integer, String> mappings = initialize_mappings();
        Stack<Integer> split_stack = new Stack<>();

        while (num != 0) {
            split_stack.push(num % 1000);
            num /= 1000;
        }

        int lvl = split_stack.size() - 1;
        String res = "";

        while(!split_stack.isEmpty()) {
            int sub_num = split_stack.pop();
            String sub_res;
            sub_res = operation_on_three(sub_num, mappings, 2);
            res = res + sub_res + ((lvl == 0 || sub_num == 0) ? "" : mappings.get((int)Math.pow(1000, lvl)));
            lvl--;
        }

        return res.trim();
    }

    public static void main(String[] args) {
        int num = 1000010;
        System.out.println(numberToWords(num));
    }
}