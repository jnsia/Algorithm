class Solution {
    public int[] solution(int[] arr, boolean[] flag) {
        int[] result = new int[10001];
        int size = 0;
        int rear = 0;
        
        for (int num: arr) {
            if (flag[size]) {
                for (int i = 0; i < num * 2; i++) {
                    result[rear] = num;
                    rear++;
                }
            } else {
                for (int i = 0; i < num; i++) {
                    if (rear > 0) {
                        rear--;
                        result[rear] = 0;
                    }
                }
            }
            size++;
        }
        
        int[] answer = new int[rear];
        
        for (int i = 0; i < rear; i++) {
            answer[i] = result[i];
        }
        
        return answer;
    }
}