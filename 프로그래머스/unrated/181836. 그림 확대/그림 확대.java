class Solution {
    public String[] solution(String[] picture, int k) {
        String[] answer = new String[picture.length * k];
        int size = 0;
        
        for (String word: picture) {
            String tmp_string = "";
            
            for (int i = 0; i < word.length(); i++) {
                char tmp = word.charAt(i);
                
                for (int j = 0; j < k; j++) {
                    tmp_string += tmp;
                }
            }
            
            for (int j = 0; j < k; j++) {
                answer[size++] = tmp_string;
            }
        }
        
        return answer;
    }
}