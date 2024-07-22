class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        String answer = "";
        
        int e = overwrite_string.length();
        char tmp;
            
        for (int i = 0; i < my_string.length(); i++) {
            if ((i >= s) && (i < e + s)) {
                tmp = overwrite_string.charAt(i - s);
                answer += tmp;
            } else {
                tmp = my_string.charAt(i);
                answer += tmp;
            } 
        }
        
        return answer;
    }
}