class Solution {
    public String solution(String s) {
        String answer = "";
        int gap = (int) 'a' - (int) 'A';
        
        int i = 0;
        int j = 0;
        
        while (i < s.length()) {
            char word = s.charAt(i);
            
            if (word == ' ') {
                answer += " ";
                i++;
                j = 0;
                continue;
            } else if (j % 2 == 0 && (int) word >= (int) 'a') {
                answer += (char) ((int) word - gap);
            } else if (j % 2 == 1 && (int) word <= (int) 'Z') {
                answer += (char) ((int) word + gap);
            } else {
                answer += word;
            }
            
            i++;
            j++;
        }
        
        System.out.println(gap);
        
        return answer;
    }
}