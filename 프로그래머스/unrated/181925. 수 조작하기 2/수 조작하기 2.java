import java.util.HashMap;

class Solution {
    public String solution(int[] numLog) {
        String answer = "";
        HashMap<Integer, String> command = new HashMap<Integer, String>(){{
            put(1, "w");
            put(-1, "s");
            put(10, "d");
            put(-10, "a");
        }};
        
        for (int i = 0; i < numLog.length - 1; i++) {
            int tmp = numLog[i + 1] - numLog[i];
            
            answer += command.get(tmp);
        }
        
        return answer;
    }
}