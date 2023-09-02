class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        int apb = Integer.parseInt(a + "" + b);
        int tab = 2 * a * b;
            
        if (apb >= tab) {
            answer = apb;
        } else {
            answer = tab;
        }
        
        return answer;
    }
}