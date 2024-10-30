class Solution {
    public int[] solution(int[] sequence, int k) {
        int[] answer = new int[2];
        
        answer[1] = sequence.length;
        
        int[] dp = new int[sequence.length + 1];
        
        for (int i = 0; i < dp.length - 1; i++) {
            dp[i + 1] = sequence[i];
            dp[i + 1] += dp[i];
        }
        
        int i = 0;
        int j = 1;
        
        while (j < dp.length) {
            while (i < dp.length) {
                int current = dp[j] - dp[i];
                
                if (current == k) {
                    if (answer[1] - answer[0] > j - i - 1) {
                        answer[0] = i;
                        answer[1] = j - 1;
                    }
                    
                    i++;
                } else if (current > k) {
                    i++;
                } else {
                    break;
                }
            }
            
            j++;
        }
        
        return answer;
    }
}