import java.lang.Math;

class Solution {
    public int solution(int sticker[]) {
        int answer = sticker[0];
        
        // 뜯었을 때, 아닐 때
        int[][] dp = new int[sticker.length][2];
        int[][] gdp = new int[sticker.length][2];
        
        // 첫 번째를 뜯었을 때
        dp[0][0] = sticker[0];
        
        for (int i = 1; i < sticker.length; i++) {
            dp[i][0] = Math.max(sticker[i] + dp[i - 1][1], dp[i - 1][0]);
            dp[i][1] = Math.max(dp[i - 1][1], dp[i - 1][0]);
        }
        
        System.out.println(dp[sticker.length - 1][1]);
        answer = Math.max(answer, dp[sticker.length - 1][1]);
                
        // 첫 번째를 안 뜯었을 때
        for (int i = 1; i < sticker.length; i++) {
            gdp[i][0] = Math.max(sticker[i] + gdp[i - 1][1], gdp[i - 1][0]);
            gdp[i][1] = Math.max(gdp[i - 1][1], gdp[i - 1][0]);
        }
        
        answer = Math.max(answer, Math.max(gdp[sticker.length - 1][0], gdp[sticker.length - 1][1]));
        System.out.println(Math.max(gdp[sticker.length - 1][0], gdp[sticker.length - 1][1]));

        return answer;
    }
}