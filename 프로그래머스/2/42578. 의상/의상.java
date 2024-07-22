import java.util.*;
import java.lang.Math;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        
        Map<String, ArrayList<String>> map = new HashMap<>();
        
        for (String[] cloth: clothes) {
            ArrayList items = map.getOrDefault(cloth[1], new ArrayList<>());
            items.add(cloth[0]);
            map.put(cloth[1], items);
        }

        for (String cloth: map.keySet()) {
            ArrayList items = map.getOrDefault(cloth, new ArrayList<>());
            answer *= items.size() + 1;          
        }
        
        return answer - 1;
    }
}