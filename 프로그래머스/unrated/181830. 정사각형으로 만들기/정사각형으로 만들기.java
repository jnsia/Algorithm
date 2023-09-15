class Solution {
    public int[][] solution(int[][] arr) {
        int width = arr[0].length;
        int height = arr.length;
        int mx_len;
        
        if (width < height) {
            mx_len = height;
        } else {
            mx_len = width;
        }
        
        int[][] answer = new int[mx_len][mx_len];
        
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {
                answer[i][j] = arr[i][j];
            }
        }
        
        return answer;
    }
}