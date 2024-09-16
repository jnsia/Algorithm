class Solution {
    public int[] solution(int n, long left, long right) {
        int diff = (int) (right - left);
        int[] answer = new int[diff + 1];

        int index = 0;
        
        for (long i = left; i <= right; i++) {
            if (i / n > i % n) {
                answer[index++] = (int) (i / n + 1);
            } else {
                answer[index++] = (int) (i % n + 1);
            }
        }
        
        return answer;
    }
}