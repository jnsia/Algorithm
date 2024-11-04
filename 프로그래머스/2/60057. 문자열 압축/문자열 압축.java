class Solution {
    public int solution(String s) {
        int answer = s.length();
        
        for (int i = 1; i < s.length(); i++) {
            String news = "";
            int count = 1;
            String prev = "";
            
            for (int j = 0; j < s.length(); j += i) {
                String word = "";
                
                for (int k = j; k < Math.min(j + i, s.length()); k++) {
                    word += s.charAt(k);
                }
                
                if (prev.equals(word)) {
                    count++;
                } else {
                    
                    if (count == 1) {
                        news += prev;
                    } else {
                        news += count + prev;
                    }
                    
                    count = 1;
                }
                
                prev = word;
            }
            
            if (count == 1) {
                news += prev;
            } else {
                news += count + prev;
            }
            
            // System.out.println(news);
            answer = Math.min(answer, news.length());
        }
        
        return answer;
    }
}