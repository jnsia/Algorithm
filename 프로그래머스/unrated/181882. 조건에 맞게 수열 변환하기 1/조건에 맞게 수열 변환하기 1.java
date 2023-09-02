class Solution {
    public int[] solution(int[] arr) {
        int[] answer = new int[arr.length];
        
        for (int idx = 0; idx < arr.length; idx++) {
            if (arr[idx] >= 50 && arr[idx] % 2 == 0) {
                answer[idx] = (int)(arr[idx] / 2);
            } else if (arr[idx] < 50 && arr[idx] % 2 == 1) {
                answer[idx] = arr[idx] * 2;
            } else {
                answer[idx] = arr[idx];
            }
        }
        
        return answer;
    }
}