import java.util.*;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        
        Map<String, Integer> wantMap = new HashMap<>();
        Map<String, Integer> discountMap = new HashMap<>();
        
        for (int i = 0; i < want.length; i++) {
            wantMap.put(want[i], -number[i]);
        }
        
        for (int i = 0; i < 10; i++) {
            if (wantMap.get(discount[i]) == null) continue;
            wantMap.put(discount[i], wantMap.get(discount[i]) + 1);
        }
        
        if (checkWant(wantMap)) answer++;
        
        for (int i = 10; i < discount.length; i++) {
            if (wantMap.get(discount[i - 10]) != null) {
                wantMap.put(discount[i - 10], wantMap.get(discount[i - 10]) - 1);
            }
            
            if (wantMap.get(discount[i]) != null) {
                wantMap.put(discount[i], wantMap.get(discount[i]) + 1);
            }
            
            if (checkWant(wantMap)) answer++;
        }
        
        return answer;
    }
    
    private boolean checkWant(Map<String, Integer> wantMap) {
        for (String want: wantMap.keySet()) {
            int number = wantMap.get(want);
            
            if (number < 0) return false;
        }
        
        return true;
    }
}