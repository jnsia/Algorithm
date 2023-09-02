import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String ans = "";
        char tmp;
        
        for (int i = 0; i < a.length(); i++) {
            tmp = a.charAt(i);
            
            if ((65 <= (int)tmp) && ((int)tmp < 91)) {
                ans += a.valueOf(tmp).toLowerCase();
            } else {
               ans += a.valueOf(tmp).toUpperCase();
            }
        }
        
        System.out.print(ans);
    }
}