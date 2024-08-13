import java.util.ArrayList;
import java.util.Collections;

public class p_2310 {
    public static int greedySum(int cur_sum, int index, ArrayList<Integer> units, int target, int count) {
        if (cur_sum == target) return count;
        if (count > 10) return -1;
        for (int i = index; i < units.size(); i++) {
            int possible_num = units.get(i);
            if (possible_num == 0) return -1;
            if (cur_sum + possible_num <= target) {
                int c = greedySum(cur_sum + possible_num, i, units, target, count + 1);
                if (c != -1) return c;
            }
        }
        return -1;
    }

    public static int minimumNumbers(int num, int k) {
        if (num == 0) return 0;
        ArrayList<Integer> units = new ArrayList<>();
        int start = k;
        while (start <= num) {
            units.add(start);
            start += 10;
        }
        Collections.reverse(units);
        return greedySum(0, 0, units, num, 0);
    }
    public static void main(String[] args) {
        int num = 947;
        int k = 2;
        System.out.println(minimumNumbers(num, k));
    }
}
