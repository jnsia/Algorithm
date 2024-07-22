class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = {0, 0};
        
        for (int i = 2; i < 2000; i++) {
            for (int j = 1; j <= i; j++) {
                int total = i * j;
                int temp = (i - 2) * (j - 2);
                
                if (total - temp == brown && temp == yellow) {
                    answer[0] = i;
                    answer[1] = j;
                    break;
                }
            }
        }
        
        return answer;
    }
}