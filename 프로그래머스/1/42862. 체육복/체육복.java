import java.util.*;

class Solution {
    
    static int[] ago = new int[31];
    
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = n - lost.length;
        
        Arrays.sort(lost);
        Arrays.sort(reserve);
        
        for (int l = 0; l < lost.length; l++) {
            for (int r = 0; r < reserve.length; r++) {
                if (lost[l] == reserve[r]) {
                    ago[lost[l]] = 1;
                    answer++;
                }
            }
        }
        
        int i = 0;
        int j = 0;
        
        while (i < lost.length && j < reserve.length) {
            if (ago[lost[i]] == 1) {
                i++;
                continue;
            }
            
            if (ago[reserve[j]] == 1) {
                j++;
                continue;
            }

            
            if (lost[i] == reserve[j] || lost[i] == reserve[j] + 1 || lost[i] == reserve[j] - 1) {
                answer++;
                i++;
                j++;
                continue;
            }
            
            if (i == lost.length) {
                j++;
                continue;
            }
            
            if (j == reserve.length) {
                i++;
                continue;
            }

            if (lost[i] == reserve[j]) {
                i++;
                j++;
            }
            else if (lost[i] > reserve[j]) {
                j++;
            } else {
                i++;
            }
        }
        
        return answer;
    }
}