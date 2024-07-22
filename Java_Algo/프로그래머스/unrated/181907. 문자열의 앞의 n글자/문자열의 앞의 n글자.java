class Solution {
    public String solution(String my_string, int n) {
        String answer = "";
        int idx = 0;
        
        while (idx < n) {
            answer += my_string.charAt(idx);
            
            idx++;
        }
        
        return answer;
    }
}