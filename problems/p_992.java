import java.util.*;

public class p_992 {
    static int subarraysWithKDistinctNaive(int[] nums, int k) {
        int count = 0;
        HashMap<Integer, Integer> k_distinct = new HashMap<>();
        int left = 0, right = 0;

        while (right < nums.length || left + k <= nums.length) {
            if (right == nums.length && left + k <= nums.length) {
                k_distinct.clear();
                left++;
                right = left;
            }

            int new_num = nums[right];
            if (k_distinct.containsKey(new_num)) {
                right++;
            } else {
                if (k_distinct.size() == k) {
                    k_distinct.clear();
                    left++;
                    right = left;
                } else {
                    k_distinct.put(new_num, 1);
                    right++;
                }
            }

            if (k_distinct.size() == k)
                count++;
            if (left + k == nums.length)
                left++;
        }
        return count;
    }

    /*
     * the idea is to use three-pointer sliding window, (left_far, left_near, right)
     */
    static int subarraysWithKDistinct(int[] nums, int k) {
        int count = 0;
        int f = 0, n = 0, r = 0;
        HashMap<Integer, Integer> k_Map = new HashMap<>();

        while (r < nums.length) {
            k_Map.put(nums[r], k_Map.getOrDefault(nums[r], 0) + 1);

            while (k_Map.size() > k) {
                k_Map.put(nums[n], k_Map.get(nums[n]) - 1);
                if (k_Map.get(nums[n]) == 0) {
                    k_Map.remove(nums[n]);
                }
                n++;
                f = n;
            }

            while (k_Map.get(nums[n]) > 1) {
                k_Map.put(nums[n], k_Map.get(nums[n]) - 1);
                n++;
            }
            
            if (k_Map.size() == k) {
                count += n - f + 1;
            }
            r++;
        }
        return count;
    }
    public static void main(String[] args) {
        int[] nums = { 2,2,2,1,3,4,1,1 };
        int k = 3;
        System.out.println(subarraysWithKDistinctNaive(nums, k));
        System.out.println(subarraysWithKDistinct(nums, k));
    }
}
