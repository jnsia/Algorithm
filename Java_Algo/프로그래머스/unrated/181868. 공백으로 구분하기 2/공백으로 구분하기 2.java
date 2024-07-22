import java.util.*;

class Solution {
    public String[] solution(String my_string) {
        List<String> answer = new ArrayList<>();
        String[] result = my_string.split(" ");
        
        for (String tmp: result) {
            if (!tmp.equals("")) {
                answer.add(tmp);
            }
        }
        
        return answer.toArray(new String[answer.size()]);
    }
}