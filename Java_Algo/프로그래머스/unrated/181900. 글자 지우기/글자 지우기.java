class Solution {
    public String solution(String my_string, int[] indices) {
        String answer = "";
        char tmp;
        boolean is_in;
        
        for (int j = 0; j < my_string.length(); j++) {
            is_in = false;
            
            for (int i = 0; i < indices.length; i++) {
                if (j == indices[i]) {
                    is_in = true;
                    break;
                }
            }
            
            if (!is_in) {
                answer += my_string.charAt(j);
            }
        }
        
        
        return answer;
    }
}