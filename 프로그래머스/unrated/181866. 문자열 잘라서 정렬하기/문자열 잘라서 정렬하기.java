import java.util.*;

class Solution {
    public String[] solution(String myString) {
        String[] result = myString.split("x");
        Arrays.sort(result);
        
        List<String> answer = new ArrayList<>();
        
        for (String tmp: result) {
            if (!tmp.equals("")) {
                answer.add(tmp);
            }
        }
        
        return answer.toArray(new String[answer.size()]);
    }
}