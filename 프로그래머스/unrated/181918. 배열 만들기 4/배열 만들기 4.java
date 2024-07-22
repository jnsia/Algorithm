class Solution {
    public int[] solution(int[] arr) {
        int[] result = new int[100001];
        int rear = 0;
            
        for (int i = 0; i < arr.length; i++) {
            if (rear == 0) {
                result[rear] = arr[i];
                rear++;
            } else if (rear > 0 && result[rear - 1] < arr[i]) {
                result[rear] = arr[i];
                rear++;
            } else if (rear > 0 && result[rear - 1] >= arr[i]) {
                result[rear - 1] = 0;
                rear--;
                i--;
            }
        }
            
        int[] stk = new int[rear];
        
        for (int i = 0; i < rear; i++) {
            stk[i] = result[i];
        }
        
        return stk;
    }
}