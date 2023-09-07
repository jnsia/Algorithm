class Solution {
    public int[] solution(int[] arr, int[][] intervals) {
        int a, b;
        int rear = 0;
        int[] res_arr = new int[100001];
        
        for (int i = 0; i < intervals.length; i++) {
            a = intervals[i][0];
            b = intervals[i][1];
            
            for (int j = a; j <= b; j++) {
                res_arr[rear] = arr[j];
                rear++;
            }
        }
        
        int[] answer = new int[rear];
        int size = 0;
        
        for (int elem: res_arr) {
            answer[size++] = elem;
            
            if (size == rear) {
                break;
            }
        }
        
        return answer;
    }
}