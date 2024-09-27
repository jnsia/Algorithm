class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        
        String[] words = {"aya", "ye", "woo", "ma"};
        
        for (String babble: babbling) {
            String temp = "";
            String prev = "";
            
            for (int i = 0; i < babble.length(); i++) {
                temp += babble.charAt(i);

                for (String word: words) {
                    if (temp.equals(word) && !temp.equals(prev)) {
                        prev = temp;
                        temp = "";
                    }
                }
            }
            
            if (temp.equals("")) answer++;
        }
        
        return answer;
    }
}