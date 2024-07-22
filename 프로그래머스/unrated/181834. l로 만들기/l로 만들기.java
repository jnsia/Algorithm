class Solution {
    public String solution(String myString) {
        String answer = "";
        
        for (int i = 0; i < myString.length(); i++) {
            char tmp = myString.charAt(i);
            
            if ((int) tmp < (int) 'l') {
                answer += 'l';
            } else {
                answer += tmp;
            }
        }
        
        return answer;
    }
}