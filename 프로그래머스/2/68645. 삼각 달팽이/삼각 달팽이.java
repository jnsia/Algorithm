class Solution {
    static int number = 1;
    
    static int[][] grid = new int[1001][1001];
    
    static int[] dx = {1, 0, -1};
    static int[] dy = {0, 1, -1};
    
    public int[] solution(int n) {
        int max = 0;
        
        for (int i = 1; i < n + 1; i++) {
            max += i;
        }
        
        int x = 0;
        int y = 0;
        int direction = 0;
        
        while (number <= max) {
            grid[x][y] = number;
            
            if (number == max) {
                break;
            }
        
            int nx = x + dx[direction];
            int ny = y + dy[direction];

            if (nx >= n || ny >= n || grid[nx][ny] > 0) {
                direction = (direction + 1) % 3;
            } else {
                number++;
                x = nx;
                y = ny;
            }
        }

        int index = 0;
        int[] answer = new int[max];
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i + 1; j++) {
                answer[index++] = grid[i][j];
            }
        }
        
        return answer;
    }
    
    private void dfs(int x, int y, int direction, int n, int max) {
        
    }
}