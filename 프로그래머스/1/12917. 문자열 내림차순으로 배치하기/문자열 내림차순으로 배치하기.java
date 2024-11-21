import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        
        int[] root = new int[s.length()];
        
        for (int i = 0; i < s.length(); i++) {
            root[i] = (int) s.charAt(i);
        }
        
        Arrays.sort(root);
        
        for (int num: root) {
            answer = (char) num + answer; 
        }
        
        return answer;
    }
}