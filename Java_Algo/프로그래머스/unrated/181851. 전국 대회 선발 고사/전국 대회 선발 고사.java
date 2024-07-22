import java.util.*;

class Solution {
    public int solution(int[] rank, boolean[] attendance) {
        int[] possible = new int[101];
        int cnt = 4;
        
        for (int i = 0; i < attendance.length; i++) {
            if (attendance[i] == true) {
                possible[rank[i]] = i + 1;
            }
        }
        
        int answer = 0;
        
        for (int i = 0; i < 101; i++) {
            if (possible[i] >= 1) {
                answer += (possible[i] - 1) * (int)Math.pow(10, cnt);
                cnt -= 2;
            }
            
            if (cnt < 0) {
                break;
            }
        }
        
        return answer;
    }
}