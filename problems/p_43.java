public class p_43 {
    public static String multiply(String num1, String num2) {
        if (num1.equals("0") || num2.equals("0")) return "0";

        int[] ans = new int[num1.length() + num2.length()];
        for (int i = num2.length() - 1; i >= 0; i--) {
            int x = num2.charAt(i) - '0';
            int index = (num1.length() + num2.length()) - (num2.length() - 1 - i) - 1;

            for (int j = num1.length() - 1; j >= 0; j--) {
                int y = num1.charAt(j) - '0';

                int prod = x * y + ans[index];
                ans[index] = prod % 10;
                ans[index - 1] += prod / 10;
                index--;
            }
        }

        int start_index = (ans[0] == 0) ? 1 : 0;
        String str = "";
        for (; start_index < (num1.length() + num2.length()); start_index++) {
            str += ans[start_index];
        }

        return str;
    }
    public static void main(String[] args) {
        String num1 = "999";
        String num2 = "999";
        System.out.println(multiply(num1, num2));
    }
}
