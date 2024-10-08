class Solution {
    public long solution(int n) {
        long answer = 0;
        
        long[] dp = new long[2001];
        
        dp[1] = 1;
        dp[2] = 2;
        
        for (int i = 3; i < 2001; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
            dp[i] = dp[i] % 1234567;
        }
        
        answer = dp[n] % 1234567;
        
        return answer;
    }
}