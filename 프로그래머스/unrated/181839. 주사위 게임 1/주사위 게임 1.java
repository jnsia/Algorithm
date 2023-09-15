class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        
        if (a % 2 == 1 && b % 2 == 1) {
            answer = a * a + b * b;
        } else if (a % 2 == 0 && b % 2 == 0) {
            if (a - b > 0) {
                answer = a - b;
            } else {
                answer = b - a;
            }
        } else {
            answer = 2 * (a + b);
        }
        
        return answer;
    }
}