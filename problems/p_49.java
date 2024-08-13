import java.util.*;

public class p_49 {
    public static List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> groups = new ArrayList<>();
        HashMap<String, Integer> all_indices = new HashMap<>();
        int index = 0;
        for (String str: strs) {
            char[] str_as_char = str.toCharArray();
            Arrays.sort(str_as_char);

            String reconstruct_str = new String(str_as_char);

            if (all_indices.get(reconstruct_str) == null) {
                all_indices.put(reconstruct_str, index);
                index++;
                groups.add(new ArrayList<>());
            }
            groups.get(all_indices.get(reconstruct_str)).add(str);
        }
        return groups;
    }

    public static void main(String[] args) {
        String[] strs = {"eat","tea","tan","ate","nat","bat"};
        List<List<String>> groups = groupAnagrams(strs);
        System.out.println(groups);
    }
}
