import java.lang.Math;

class Solution {
    
    static int[][] board = new int[501][501];
    
    public int solution(int[][] triangle) {
        int answer = 0;
        
        for (int i = 0; i < triangle.length; i++) {
            int[] row = triangle[i];
            
            for (int j = 0; j < row.length; j++) {
                board[i][j + 1] = row[j];
            }
        }
        
        for (int i = 1; i < triangle.length; i++) {
            for (int j = 1; j < i + 2; j++) {
                board[i][j] += Math.max(board[i - 1][j - 1], board[i - 1][j]);
            }
        }
        
        for (int i = 1; i < triangle.length + 1; i++) {
            answer = Math.max(board[triangle.length - 1][i], answer);
        }
        
        return answer;
    }
}