import java.util.HashMap;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        
        HashMap<String, Integer> map = new HashMap<>();
        
        for (int i = 0; i < participant.length; i++) {
            map.put(participant[i], map.getOrDefault(participant[i], 0) + 1);
        }
        
        for (String person: completion) {
            map.put(person, map.get(person) - 1);
        }
        
        for (int i = 0; i < participant.length; i++) {
            int result = map.get(participant[i]);
            
            if (result > 0) answer = participant[i];
        }
        
        return answer;
    }
}