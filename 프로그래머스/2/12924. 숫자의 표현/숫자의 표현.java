class Solution {
    public int solution(int n) {
        int answer = 0;
        
        int[] dp = new int[n + 1];
        
        for (int i = 0; i < n + 1; i++) {
            dp[i] = i;
        }
        
        for (int i = 1; i < n + 1; i++) {
            dp[i] += dp[i - 1];
        }
        
        int i = 0;
        int j = 1;
        
        while (j < n + 1) {
            int temp = dp[j] - dp[i];
            // System.out.println(temp + " " + i + " " + j);
            
            if (temp > n) {
                i++;
            } else if (temp == n) {
                answer++;
                i++;
                j++;
            } else {
                j++;
            }
        }
        
        return answer;
    }
}