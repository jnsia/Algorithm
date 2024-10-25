class Solution {
    public long solution(int[] sequence) {
        long answer = 0;
        
        long[] dp1 = new long[sequence.length];
        long[] dp2 = new long[sequence.length];
        
        dp1[0] = sequence[0];
        dp2[0] = -1 * sequence[0];
        answer = Math.max(dp1[0], dp2[0]);
        
        for (int i = 1; i < dp1.length; i++) {
            dp1[i] = Math.max(sequence[i], dp2[i - 1] + sequence[i]);
            dp2[i] = Math.max(-1 * sequence[i], dp1[i - 1] - sequence[i]);
            
            answer = Math.max(answer, dp1[i]);
            answer = Math.max(answer, dp2[i]);
        }
        
        return answer;
    }
}