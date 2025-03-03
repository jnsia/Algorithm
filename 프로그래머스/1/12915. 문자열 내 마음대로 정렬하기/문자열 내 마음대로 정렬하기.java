import java.util.*;

class Solution {
    public String[] solution(String[] strings, int n) {
        String[] answer = {};
        
        for (int i = 0; i < strings.length - 1; i++) {
            for (int j = i + 1; j < strings.length; j++) {
                char first = strings[i].charAt(n);
                char second = strings[j].charAt(n);
                
                if (first > second) {
                    String temp = strings[i];
                    strings[i] = strings[j];
                    strings[j] = temp;
                } else if (first == second && strings[i].compareTo(strings[j]) >= 0) {
                    String temp = strings[i];
                    strings[i] = strings[j];
                    strings[j] = temp;
                }
            }
        }
        
        for (int i = 0; i < strings.length; i++) {
            System.out.print(strings[i] + " ");
        }
        
        return strings;
    }
}