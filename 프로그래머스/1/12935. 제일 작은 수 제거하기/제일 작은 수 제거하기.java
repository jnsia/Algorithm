class Solution {
    public int[] solution(int[] arr) {
        if (arr.length == 1) return new int[] {-1};        
        
        int[] answer = new int[arr.length - 1];
        
        int minValue = 10000001;
        int minValueIndex = arr.length;
        
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] < minValue) {
                minValue = arr[i];
                minValueIndex = i;
            }
        }
        
        int index = 0;
        
        for (int i = 0; i < arr.length; i++) {
            if (i != minValueIndex) {
                answer[index++] = arr[i];
            }
        }
        
        return answer;
    }
}