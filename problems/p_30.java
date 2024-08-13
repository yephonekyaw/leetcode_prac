import java.util.*;

public class p_30 {
    public static List<Integer> findSubstring(String s, String words[]) {
        List<Integer> indices = new ArrayList<>();
        
        return indices;
    }

    public static void main(String[] args) {
        String s = "wordgoodgoodgoodbestword";
        String words[] = {"word","good","best","good"};
        List<Integer> indices = findSubstring(s, words);
        for (int i: indices) {
            System.out.print(i + " ");
        }
    }
}
