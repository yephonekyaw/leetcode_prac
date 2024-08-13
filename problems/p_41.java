public class p_41 {
    public static int firstMissingPositive(int[] nums) {
        // HashMap<Integer, Integer> preNum = new HashMap<>();
        // int min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;
        // for (int i = 0; i < nums.length; i++) {
        //     if (nums[i] > 0) {
        //         preNum.put(nums[i], i);
        //         min = Math.min(nums[i], min);
        //     }
        //     max = Math.max(nums[i], max);
        // }
        
        // if (min > 1 || max <= 0) return 1;
        // while (true) {
        //     if (preNum.get(min) == null) return min;
        //     min++;
        // }

        int n = nums.length;
        boolean[] seen = new boolean[n + 1];

        for (int num: nums) {
            if (num > 0 && num <= n) seen[num] = true;
        }

        for (int i = 1; i <= n; i++) {
            if (!seen[i]) return i;
        }
        return n + 1;
    }

    public static void main(String[] args) {
        int[] nums = {1,2,3,4,5,6,7,8,9,20};
        System.out.println(firstMissingPositive(nums));
    }
}
