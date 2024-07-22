class Solution {
    public String solution(String code) {
        String answer = "";
        int mode = 0;
        char tmp;
        
        for (int i = 0; i < code.length(); i++) {
            tmp = code.charAt(i);
            
            if (tmp == '1') {
                mode = (mode + 1) % 2;
            } else {
                if (mode == 1 && i % 2 == 1) {
                    answer += tmp;
                } else if (mode == 0 && i % 2 == 0) {
                    answer += tmp;
                }
            }
        }
        
        if (answer.length() == 0) {
            answer = "EMPTY";
        }
        
        return answer;
    }
}