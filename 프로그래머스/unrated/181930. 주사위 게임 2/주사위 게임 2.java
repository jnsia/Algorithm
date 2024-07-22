class Solution {
    public int power(int num, int times) {
        int result = 1;
            
        for (int i = 0; i < times; i++) {
            result *= num;
        }
        
        return result;
    }
    
    public int solution(int a, int b, int c) {
        int answer = 0;
        
        if (a == b && b == c) {
            answer = (a + b + c) * (power(a, 2) + power(b, 2) + power(c, 2)) * (power(a, 3) + power(b, 3) + power(c, 3));
        } else if (a == b || a == c || b == c) {
            answer = (a + b + c) * (power(a, 2) + power(b, 2) + power(c, 2));
        } else {
            answer = a + b + c;
        }
        
        return answer;
    }
}