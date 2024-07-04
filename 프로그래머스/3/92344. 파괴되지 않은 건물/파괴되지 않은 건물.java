class Solution {
    
    // 1001 X 1001
    // type, r1, c1, r2, c2, degree
    // 1 = 공격
    // 0 = 회복
    
    public int solution(int[][] board, int[][] skill) {
        int answer = 0;
        
        int N = board.length;
        int M = board[0].length;
        
        int[][] map = new int[N + 1][M + 1];
        
        for (int[] info: skill) {
            int type = (info[0] == 1) ? -1 : 1;
            
            int r1 = info[1];
            int c1 = info[2];
            int r2 = info[3];
            int c2 = info[4];
            
            int degree = info[5];
            
            map[r1][c1] += degree * type;
            map[r1][c2 + 1] -= degree * type;
            map[r2 + 1][c1] -= degree * type;
            map[r2 + 1][c2 + 1] += degree * type;
        }
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                map[i][j + 1] += map[i][j];
            }
        }
        
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                map[j + 1][i] += map[j][i];
            }
        }
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (board[i][j] + map[i][j] > 0) answer++;
            }
        }
        
        return answer;
    }
}