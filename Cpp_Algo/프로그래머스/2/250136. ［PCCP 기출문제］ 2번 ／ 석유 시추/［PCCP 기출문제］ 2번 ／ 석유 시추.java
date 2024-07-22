import java.lang.Math;

class Solution {
    static int height;
    static int width;
    
    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, 1, 0, -1};
    
    static int cnt = 1;
    static int[] memo = new int[50001];
    static int result = 0;
    static int[][] visited = new int[501][501];
    
    public int solution(int[][] land) {
        int answer = 0;
        
        height = land.length;
        width = land[0].length;
        
        for (int i = 0; i < width; i++) {
            int temp = 0;
            int[] cntVisit = new int[50001];
            
            for (int j = 0; j < height; j++) {
                if (land[j][i] == 1 && visited[j][i] == 0) {
                    result = 0;
                    visited[j][i] = cnt;
                    dfs(land, j, i);
                    cntVisit[visited[j][i]] = 1;
                    memo[cnt] = result;
                    cnt++;
                    temp += result;
                } else if (visited[j][i] > 0 && cntVisit[visited[j][i]] == 0) {
                    temp += memo[visited[j][i]];
                    cntVisit[visited[j][i]] = 1;
                }
            }
            
            answer = Math.max(answer, temp);
        }

        return answer;
    }
    
    public void dfs(int[][] land, int x, int y) {
        result += 1;
        
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if (nx < 0 || nx >= height || ny < 0 || ny >= width) continue;
            if (visited[nx][ny] > 0 || land[nx][ny] == 0) continue;
            
            visited[nx][ny] = cnt;
            dfs(land, nx, ny);
        }
    }
}