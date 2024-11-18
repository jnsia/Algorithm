class Solution {
    public int solution(int[] absolutes, boolean[] signs) {
        int answer = 0;
        
        for (int idx = 0; idx < absolutes.length; idx++) {
            if (signs[idx]) answer += absolutes[idx];
            else answer -= absolutes[idx];
        }      
        
        return answer;
    }
}