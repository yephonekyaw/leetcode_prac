import java.util.*;
/**
 * p_150
 */
public class p_150 {
    static int[] popStack(Stack<Integer> stack) {
        return new int[]{stack.pop(), stack.pop()};
        // 0, 1
    }

    static int evalRPN(String[] tokens) {
        Stack<Integer> operand_stack = new Stack<>();
        for (int i = 0; i < tokens.length; i++) {
            int[] operands;
            switch (tokens[i]) {
                case "+":
                    operands = popStack(operand_stack);
                    operand_stack.push(operands[1] + operands[0]);
                    break;
                case "-":
                    operands = popStack(operand_stack);
                    operand_stack.push(operands[1] - operands[0]);
                    break;
                case "*":
                    operands = popStack(operand_stack);
                    operand_stack.push(operands[1] * operands[0]);
                    break;
                case "/":
                    operands = popStack(operand_stack);
                    operand_stack.push(operands[1] / operands[0]);
                    break;
                default:
                    operand_stack.push(Integer.valueOf(tokens[i]));
            }
        }

        return operand_stack.pop();
    }

    public static void main(String[] args) {
        String[] tokens = {"2", "1", "+", "3", "*"};
        System.out.println(evalRPN(tokens));
    }
}