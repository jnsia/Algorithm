import java.util.HashMap;

class Solution {
    public int solution(int n, String control) {
        int answer = n;
        char command;
        HashMap<String, Integer> map = new HashMap<String, Integer>();
        map.put("w", 1);
        map.put("s", -1);
        map.put("d", 10);
        map.put("a", -10);

        for (int i = 0; i < control.length(); i++) {
            command = control.charAt(i);
            answer += map.get(String.valueOf(command));
        }
        
        return answer;
    }
}