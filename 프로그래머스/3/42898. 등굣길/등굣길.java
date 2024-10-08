class Solution {
    
    static int mod = 1000000007;
    
    public int solution(int m, int n, int[][] puddles) {
        int answer = 0;
        
        int[][] puddleMap = new int[n + 1][m + 1];
        int[][] dp = new int[n + 1][m + 1];
        
        for (int[] puddle: puddles) {
            puddleMap[puddle[1]][puddle[0]] = -1;
        }
        
        dp[1][1] = 1;
    
        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < m + 1; j++) {
                if (puddleMap[i][j] == -1) continue;
                int temp = (dp[i - 1][j] % mod + dp[i][j - 1] % mod) % mod;
                dp[i][j] += temp % mod;
            }
        }
        
        answer = dp[n][m] % mod;
        
        return answer;
    }
}