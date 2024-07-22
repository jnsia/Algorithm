class Solution {
    public int[] solution(int n, int[] slicer, int[] num_list) {
        int[] answer = new int[101];
        int rear = 0;
        
        if (n == 1) {
            for (int i = 0; i <= slicer[1]; i++) {
                answer[i] = num_list[i];
                rear++;
            }
        }
        
        if (n == 2) {
            for (int i = slicer[0]; i < num_list.length; i++) {
                answer[i - slicer[0]] = num_list[i];
                rear++;
            }
        }
        
        if (n == 3) {
            for (int i = slicer[0]; i <= slicer[1]; i++) {
                answer[i - slicer[0]] = num_list[i];
                rear++;
            }
        }
        
        if (n == 4) {
            for (int i = slicer[0]; i <= slicer[1]; i += slicer[2]) {
                answer[(i - slicer[0]) / slicer[2]] = num_list[i];
                rear++;
            }
        }
        
        int[] result = new int[rear];
        
        for (int i = 0; i < rear; i++) {
            result[i] = answer[i];
        }
        
        return result;
    }
}