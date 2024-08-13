import java.util.HashMap;
public class p_3 {
    public static int perform(String s) {
        int max_len = 0;
        HashMap<Character, Integer> unique_seq = new HashMap<>();
        int start = 0, cur_len = 0;
        for (int i = 0; i < s.length(); i++) {
            if (!unique_seq.containsKey(s.charAt(i))) {
                unique_seq.put(s.charAt(i), i);
                cur_len++;
                max_len = Math.max(max_len, cur_len);
            } else {
                // since we don't remove repeated characters, it is also possible that
                // the current char is inside the unique_seq, but it is not in our current substring
                int possible_last_char_index = unique_seq.get(s.charAt(i));
                start = Math.max(start, possible_last_char_index + 1);
                cur_len = i - start + 1;
                max_len = Math.max(max_len, cur_len);
                unique_seq.put(s.charAt(i), i);
            }
        }
        return max_len;
    }

    public static void main(String[] args) {
        String s = "abba";
        System.out.println(perform(s));
    }
}