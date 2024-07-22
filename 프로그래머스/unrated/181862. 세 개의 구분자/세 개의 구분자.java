import java.util.*;

class Solution {
    public String[] solution(String myStr) {
        List<String> answer = new ArrayList<>();
        String tmp = "";
        
        for (int i = 0; i < myStr.length(); i++) {
            char chr = myStr.charAt(i);
            
            if ((chr == 'a') || (chr == 'b') || (chr == 'c')) {
                if (!tmp.equals("")) {
                    answer.add(tmp);
                }
                tmp = "";
                
            } else {
                tmp += chr;
            }
        }
        
        if (!tmp.equals("")) {
            answer.add(tmp);
        }
        
        if (answer.size() == 0) {
            answer.add("EMPTY");
        }
        
        return answer.toArray(new String[answer.size()]);
    }
}