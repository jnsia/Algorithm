class Solution {
    public boolean solution(int x) {
        boolean answer = false;
        
        int sum = 0;
        int origin = x;
        
        while (x > 0) {
            sum += x % 10;
            x /= 10;    
        }
        
        if (origin % sum == 0) answer = true;
        
        return answer;
    }
}