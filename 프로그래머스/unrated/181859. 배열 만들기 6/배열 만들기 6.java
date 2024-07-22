class Solution {
    public int[] solution(int[] arr) {
        int[] stk = new int[1000001];
        int rear = 0;
        
        for (int i = 0; i < arr.length; i++) {
            if (rear == 0) {
                stk[rear] = arr[i];
                rear++;
            } else if (stk[rear - 1] == arr[i]) {
                stk[rear - 1] = 0;
                rear--;
            } else {
                stk[rear] = arr[i];
                rear++;
            }
        }
        
        int size = 0;
        
        if (rear == 0) {
            int[] answer = new int[1];
            answer[0] = -1;
            return answer;
        }
        
        int[] answer = new int[rear];

        for (int num: stk) {
            answer[size++] = num;

            if (size >= rear) {
                break;
            }
        }
        
        return answer;
    }
}