class Solution {
    public String solution(String s) {
        String answer = "";
        
        s = s.toLowerCase();
        
        // 65 ~ 90 => 대문자
        // 97 ~ 122 => 소문자
        
        // for (int i = 0; i < 125; i++) {
        //     System.out.println((char) i + " " + i); 
        // }

        char firstWord = s.charAt(0);
        
        if ((int) firstWord >= 97 && (int) firstWord <= 122) {
            s = (s.charAt(0) + "").toUpperCase() + s.substring(1);
        }
        
        Boolean temp = false;
        
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) == ' ') {
                temp = true;
                continue;
            }
            
            if (temp) {
                if ((int) s.charAt(i) >= 97 && (int) s.charAt(i) <= 122) {
                    s = s.substring(0, i) + (char) ((int) s.charAt(i) - 32) + s.substring(i + 1);
                }
                
                temp = false;
            }
        }
        
        System.out.println(s);
        answer = s;
        
        return answer;
    }
}