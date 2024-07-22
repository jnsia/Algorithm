class Solution {
    public int solution(String my_string, String is_suffix) {
        int answer = 0;
        int suffix_index = my_string.length() - is_suffix.length();
        
        if (suffix_index < 0) {
            return answer;
        }
        
        if (my_string.indexOf(is_suffix, suffix_index) >= 0) {
            answer = 1;
        }
        
        return answer;
    }
}