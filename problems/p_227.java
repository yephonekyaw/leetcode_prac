import java.util.*;

class Solution {
    public int calculate(String s) {
        Stack<Integer> operand_stack = new Stack<>();
        Queue<String> operator_que = new LinkedList<>();

        s = s.replaceAll("\s", "");
        
        int i = 0;
        while (i < s.length()) {
            int a, b;
            switch (s.charAt(i) + "") {
                case "*":
                    a = operand_stack.pop();
                    int k = i + 1;
                    while(k < s.length() && (int)s.charAt(k) >= 48 && (int)s.charAt(k) <= 57) k++;
                    b = Integer.valueOf(s.substring(i + 1, k));
                    operand_stack.push(a * b);
                    i += (k - i);
                    break;
                case "/":
                    a= operand_stack.pop();
                    int e = i + 1;
                    while (e < s.length() && (int)s.charAt(e) >= 48 && (int)s.charAt(e) <= 57) e++;
                    b = Integer.valueOf(s.substring(i + 1, e));
                    operand_stack.push(a / b);
                    i += (e - i);
                    break;
                case "+":
                    operator_que.add("+");
                    i++;
                    break;
                case "-":
                    operator_que.add("-");
                    i++;
                    break;
                default:
                    int j = i + 1;
                    while(j < s.length() && (int)s.charAt(j) >= 48 && (int)s.charAt(j) <= 57) j++;
                    operand_stack.push(Integer.valueOf(s.substring(i, j)));
                    i += s.substring(i, j).length();
                    break;
            }
        }

        Stack<Integer> new_op_st = new Stack<>();
        while(!operand_stack.isEmpty()) new_op_st.add(operand_stack.pop());
        
        System.out.println(new_op_st);
        
        while(!operator_que.isEmpty()) {
            int x = new_op_st.pop();
            int y = new_op_st.pop();
            switch (operator_que.remove()) {
                case "+":
                    new_op_st.push(x + y);
                    break;
                case "-":
                    new_op_st.push(x - y);
                    break;
            }
        }
        return new_op_st.pop();
    }
}

public class p_227 {
    public static void main(String[] args) {   
    }
}
