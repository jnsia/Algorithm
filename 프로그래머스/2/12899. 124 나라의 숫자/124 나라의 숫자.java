class Solution {
    public String solution(int n) {
        String answer = "";
        
        String[] pattern = {"1", "2", "4"};
        
        // n = n - 1;
        
        while (n > 0) {
            int m = (n - 1) / 3;
            int l = (n - 1) % 3;
            
            // System.out.println(m + " " + l);
            
            answer = pattern[l] + answer;
            
            n = m;
        }
        
        return answer;
    }
}