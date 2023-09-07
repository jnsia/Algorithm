class Solution {
    public int[] solution(int[] arr) {
        int front = -1;
        int rear = -1;
        
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == 2) {
                if (front == -1) {
                    front = i;
                    rear = i;
                } else {
                    rear = i;
                }
            }
        }
        
        System.out.println(front);
        System.out.println(rear);
        
        int[] answer = new int[rear - front + 1];
        
        if (front == -1 && rear == -1) {
            answer[0] = -1;
        } else {
            for (int i = front; i <= rear; i++) {
                answer[i - front] = arr[i];
            }
        }
        
        return answer;
    }
}