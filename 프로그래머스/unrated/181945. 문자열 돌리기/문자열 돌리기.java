import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        char tmp;
        
        for (int i = 0; i < a.length(); i++) {
            tmp = a.charAt(i);
            System.out.println(tmp);
        }
    }
}