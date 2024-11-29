class Solution {
    public int solution(String s) {
        int answer = 0;
        boolean isNegative = false;
        
        if (s.charAt(0) == '-') {
            isNegative = true;
            s = s.replace("-", "");
        } else if (s.charAt(0) == '+') {
            s = s.replace("+", "");
        }
        
        for (int i = 0; i < s.length(); i++) {
            answer *= 10;
            
            char word = s.charAt(i);
            
            if (word == '-') {
                answer *= -1;
            } else {
                answer += (int) word - (int) '0';
            }
        }
        
        if (isNegative) answer *= -1;
        
        return answer;
    }
}