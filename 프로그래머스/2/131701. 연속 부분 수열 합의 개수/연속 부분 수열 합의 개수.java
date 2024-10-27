import java.util.*;

class Solution {
    public int solution(int[] elements) {
        int answer = 0;
        
        Set<Integer> set = new HashSet<>();
        
        int length = 1;
        
        while (length <= elements.length) {
            int current = 0;
            
            for (int i = 0; i < length; i++) {
                current += elements[i];
            }
            
            set.add(current);
            
            int end = elements.length + length - 1;
            
            for (int i = length; i < end; i++) {
                current -= elements[i - length];
                current += elements[i % elements.length];
                // System.out.println(current);
                
                set.add(current);
            }
            
            length++;
        }
        
        answer = set.size();
        // System.out.println(set);
        
        return answer;
    }
}