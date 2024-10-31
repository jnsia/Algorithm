import java.util.*;

class Solution {
    public int solution(int[] A, int[] B) {
        int answer = 0;
        
        Arrays.sort(A);
        Arrays.sort(B);
        
        int front = 0;
        int rear = B.length - 1;
        
        for (int i = A.length - 1; i >= 0; i--) {
            if (A[i] >= B[rear]) {
                front++;
            } else {
                answer++;
                rear--;
            }
        }
        
        return answer;
    }
}