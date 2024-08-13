import java.util.*;

public class p_60 {
    public static void find_permutation(int[] tmp_cp, int[] tmp_permu, int index, ArrayList<String> final_permu) {
        if (index >= tmp_cp.length) {
            String each_permu = "";
            for (int x: tmp_permu) {
                each_permu += x;
            }
            final_permu.add(each_permu);
            return;
        }

        for (int i = 0; i < tmp_cp.length; i++) {
            if (tmp_cp[i] != 0) {
                tmp_permu[index] = tmp_cp[i];
                index++;
                tmp_cp[i] = 0;
                find_permutation(tmp_cp, tmp_permu, index, final_permu);
                index--;
                tmp_cp[i] = tmp_permu[index];
            }
        }
    }

    public static String getPermutation(int n, int k) {
        int[] og_mat = new int[n];
        int total_permu = 1;
        for (int i = 0; i < n; og_mat[i] = i + 1, i++, total_permu *= i);
        ArrayList<String> final_permu = new ArrayList<>();

        int start_ele = (k - 1) / (total_permu / n);
        int[] tmp_cp = og_mat.clone();
        int[] tmp_permu = new int[n];
        tmp_permu[0] = tmp_cp[start_ele];
        tmp_cp[start_ele] = 0;
        find_permutation(tmp_cp, tmp_permu, 1, final_permu);

        // for (int i = 0; i < n; i++) {
        //     if (final_permu.size() >= k) break;
            
        //     int[] tmp_cp = og_mat.clone();
        //     int[] tmp_permu = new int[n];
        //     tmp_permu[0] = tmp_cp[i];
        //     tmp_cp[i] = 0;
        //     find_permutation(tmp_cp, tmp_permu, 1, final_permu);
        // }

        int x = 0;
        String ans = "";
        k = (k - 1) % (total_permu / n);

        for (String str: final_permu) {
            if (x == k) {
                ans = str;
                break;
            }
            x++;
        }
        return ans;
    }

    public static void main(String[] args) {
        int size = 3;
        int index = 3;
        System.out.println(getPermutation(size, index));
    }
}