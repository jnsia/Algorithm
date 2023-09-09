class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        
        myString = myString.toLowerCase();
        pat = pat.toLowerCase();
        System.out.print(myString);
        
        if (myString.indexOf(pat) >= 0) {
            answer = 1;
        }
        
        return answer;
    }
}