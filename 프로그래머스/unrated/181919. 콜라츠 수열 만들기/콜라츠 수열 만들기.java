class Solution {
    public int[] solution(int n) {
        int[] result = new int[1001];
        int front = 0;
        int rear = 1;
        int idx = 0;
        int target = n;
        
        while (target > 1) {
            if (target % 2 == 0) {
                target = target / 2;
            } else {
                target = target * 3 + 1;
            }
            
            result[idx] = target;
            
            idx++;
            rear++;
        }
        
        int[] answer = new int[rear];
        answer[0] = n;
        
        for (int i = 1; i < rear; i++) {
            answer[i] = result[i - 1];
        }
        
        return answer;
    }
}