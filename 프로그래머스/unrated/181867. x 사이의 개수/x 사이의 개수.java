import java.util.*;

class Solution {
    public int[] solution(String myString) {
        List<Integer> answer = new ArrayList<>();
        int cnt = 0;
        
        for (int i = 0; i < myString.length(); i++) {
            char tmp = myString.charAt(i);
            
            if (tmp != 'x') {
                cnt++;
            } else {
                answer.add(cnt);
                cnt = 0;
            }
        }
        
        answer.add(cnt);
        
        return answer.stream().mapToInt(x -> x).toArray();
    }
}