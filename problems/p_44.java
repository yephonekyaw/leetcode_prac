import java.util.Scanner;

public class p_44 {
  public static boolean isMatch(String s, String p) {
    int m = s.length(), n = p.length(), i = 0, j = 0, last_wildcard = -1, last_match = 0;
    while (i < m) {
      if (j < n && (s.charAt(i) == p.charAt(j) || p.charAt(j) == '?')) {
        i++;
        j++;
      } else if (j < n && p.charAt(j) == '*') {
        last_wildcard = j;
        last_match = i;
        j++;
      } else if (last_wildcard != -1) {
        j = last_wildcard + 1;
        last_match += 1;
        i = last_match;
      } else {
        return false;
      }
    }
    // if there are extra asterisk left in the pattern
    while (j < n && p.charAt(j) == '*') {
      j++;
    }
    return j == n;
  }

  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    String s = scan.nextLine();
    String t = scan.nextLine();
    boolean isMatch = isMatch(s, t);
    System.out.println(isMatch);
    scan.close();
  }
}