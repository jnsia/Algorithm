import java.util.*;

class Solution {
    public int[] solution(int[] arr, int k) {
        int[] answer = new int[k];
        
        for (int i = 0; i < answer.length; i++) {
            answer[i] = -1;
        }
        
        int rear = 0;
        
        for (int num: arr) {
            boolean is_contain = false;

            for (int i = 0; i < answer.length; i++) {
                if (answer[i] == num) {
                    is_contain = true;
                    break;
                }
            }
            
            if (!is_contain) {
                answer[rear] = num;
                rear++;
            }
            
            if (rear == k) {
                break;
            }
            
        }
        
        return answer;
    }
}