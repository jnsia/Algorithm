class Solution {
    public String solution(String myString) {
        String answer = "";
        char tmp;
        
        myString = myString.toLowerCase();
        answer = myString.replace("a", "A");
                
        return answer;
    }
}