import java.util.*;

class Solution {
    public int solution(String str1, String str2) {
        int answer = 0;
        
        str1 = str1.toLowerCase();
        str2 = str2.toLowerCase();
        
        System.out.println(str1 + " " + str2);
        
        Map<String, Integer> str1Map = new HashMap<>();
        Map<String, Integer> str2Map = new HashMap<>();
        Map<String, Integer> totalMap = new HashMap<>();
        
        double sum = 0;
        double total = 0;
        
        for (int i = 0; i < str1.length() - 1; i++) {
            char first = str1.charAt(i);
            char second = str1.charAt(i + 1);
            
            if (first < 97 || first > 122) continue;
            if (second < 97 || second > 122) continue;
                        
            String word = first + "" + second;
            
            str1Map.put(word, str1Map.getOrDefault(word, 0) + 1);
            total++;
        }
        
        for (int i = 0; i < str2.length() - 1; i++) {
            char first = str2.charAt(i);
            char second = str2.charAt(i + 1);
            
            if (first < 97 || first > 122) continue;
            if (second < 97 || second > 122) continue;
            
            System.out.println(first + "" + second);
            
            String word = first + "" + second;
            
            str2Map.put(word, str2Map.getOrDefault(word, 0) + 1);
            total++;
        }
        
        for (String key: str1Map.keySet()) {
            if (str2Map.get(key) == null) continue;
            
            int str1Count = str1Map.get(key);
            int str2Count = str2Map.get(key);
            
            sum += Math.min(str1Count, str2Count);
            // System.out.println(str1Count + " " + str2Count);
        }
        
        double result;
        
        if (total - sum > 0) {
            result = (sum / (total - sum)) * 65536;
        } else {
            result = 65536;
        }

        answer = (int) result;
        
        return answer;
    }
}