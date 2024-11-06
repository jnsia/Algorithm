import java.util.*;

class Solution {
    public long solution(int[] weights) {
        long answer = 0;
        
        Map<Integer, Integer> map = new HashMap<>();
        
        for (int i = 0; i < weights.length; i++) {
            map.put(weights[i], map.getOrDefault(weights[i], 0) + 1);
        }
        
        for (int weight1: map.keySet()) {
            for (int weight2: map.keySet()) {
                if (weight1 == weight2) {
                    continue;
                }
                if(check(weight1, weight2)) {
                    answer += (long) map.get(weight1) * (long) map.get(weight2);
                };
            }    
        }
        
        answer /= 2;
        
        for (int weight1: map.keySet()) {
            answer += (long) map.get(weight1) * (long) (map.get(weight1) - 1) / 2;
            // System.out.println(weight1 + " " + answer);
        }
        
        return answer;
    }
    
    private Boolean check(int weight1, int weight2) {
        for (int i = 2; i < 5; i++) {
            for (int j = 2; j < 5; j++) {
                if (weight1 * i == weight2 * j) {
                    return true;
                }
            }    
        }
        
        return false;
    }
}