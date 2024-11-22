class Solution {
    public boolean solution(String s) {
        boolean answer = true;
        
        if (s.length() == 4 || s.length() == 6) {
            for (int i = 0; i < s.length(); i++) {
                char word = s.charAt(i);
            
                if ((int) '0' > (int) word || (int) '9' < word) {
                    answer = false;
                    break;
                }
            }    
        } else {
            answer = false;
        }
        
        return answer;
    }
}