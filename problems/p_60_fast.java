public class p_60_fast {
    public static String find_Kth_permutation(String seq, int total_permu_count, int k) {
        if (seq.length() == 1) {
            return seq.charAt(0) + "";
        }

        int total_per_each_num = total_permu_count / seq.length();
        int cur_ele_index = (k - 1) / total_per_each_num;

        /*
         * Basically, what this if condition does is finding a new key for the next iteration
         * For example, we want to find index = 9 and size = 4
         * 1st iteration: index is 9
         * 2nd iteration: index is 3
         * 3rd iteration: index is 1
         * 4th iteration: return charAt(0) since seq.length() == 1
         * 
         * Another example, index = 6 and size = 6
         * 1st iteration: index is 6
         * 2nd iteration: index is 6 again
         * 3rd iteration: index is 2
         * 4th iteration: return charAt(0) since seq.length() == 1
         * 
         * 10 4 2 0
         * 11 5 1 0
         * 12 6 2 0
         */
        if (k % total_per_each_num == 0) {
            k = total_per_each_num;
        } else {
            k = k % total_per_each_num;
        }
        return seq.charAt(cur_ele_index) + find_Kth_permutation(seq.substring(0, cur_ele_index) + seq.substring(cur_ele_index + 1), total_permu_count / seq.length(), k);
    }

    public static String getPermutation(int n, int k) {
        String seq = "";
        int total_permu_count = 1;
        for (int i = 1; i <= n; seq += i, total_permu_count *= i, i++);
        return (find_Kth_permutation(seq, total_permu_count, k));
    }
    public static void main(String[] args) {
        int size = 4;
        int index = 10;
        System.out.println(getPermutation(size, index));
    }
}
