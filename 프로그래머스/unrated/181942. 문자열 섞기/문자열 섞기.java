class Solution {
    public String solution(String str1, String str2) {
        String answer = "";
        char tmp1;
        char tmp2;
        
        for (int i = 0; i < str1.length(); i++) {
            tmp1 = str1.charAt(i);
            tmp2 = str2.charAt(i);
            answer += tmp1;
            answer += tmp2;
        }
        
        return answer;
    }
}