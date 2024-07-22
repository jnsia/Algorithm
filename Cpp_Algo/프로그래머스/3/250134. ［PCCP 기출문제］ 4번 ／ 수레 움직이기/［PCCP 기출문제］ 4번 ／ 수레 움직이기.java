import java.lang.Math;

class Solution {
    
    static int[] dx = { 1, 0, -1, 0 };
    static int[] dy = { 0, 1, 0, -1 };
    
    static int[][] rvisited = new int[4][4];
    static int[][] bvisited = new int[4][4];
    
    static int minTurn = 1000;
    
    static int erx = -1;
    static int ery = -1;
    static int ebx = -1;
    static int eby = -1;
    static int h;
    static int w;
    
    public int solution(int[][] maze) {
        int answer = 0;
        
        h = maze.length;
        w = maze[0].length;
    
        int srx = -1;
        int sry = -1;
        int sbx = -1;
        int sby = -1;
        
        // 0은 빨간맛 1은 파란만장한 나의 삶!
        // color + 3은 돌아가야 할 품...
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                if (maze[i][j] == 1) {
                    srx = i;
                    sry = j;
                }
                
                if (maze[i][j] == 2) {
                    sbx = i;
                    sby = j;
                }
                
                if (maze[i][j] == 3) {
                    erx = i;
                    ery = j;
                }
                
                if (maze[i][j] == 4) {
                    ebx = i;
                    eby = j;
                }
                
                if (maze[i][j] == 5) {
                    rvisited[i][j] = 1;
                    bvisited[i][j] = 1;
                }
            }    
        }
        
        rvisited[srx][sry] = 1;
        bvisited[sbx][sby] = 1;
        
        dfs(srx, sry, sbx, sby, 0);
        
        if (minTurn != 1000) {
            answer = minTurn;
        }
        
        return answer;
    }

    public void dfs(int rx, int ry, int bx, int by, int turn) {
        if (rx == erx && ry == ery && bx == ebx && by == eby) {
            minTurn = Math.min(minTurn, turn);
            return;
        }
        
        if (turn > 100) return;
        
        for (int i = 0; i < 4; i++) {
            int nrx = rx + dx[i];
            int nry = ry + dy[i];
            
            if (rx == erx && ry == ery) {
                nrx = rx;
                nry = ry;
            } else {
                if (nrx < 0 || nrx >= h || nry < 0 || nry >= w) continue;
                if (rvisited[nrx][nry] == 1) continue;
            }
            
            for (int j = 0; j < 4; j++) {
                int nbx = bx + dx[j];
                int nby = by + dy[j];
                
                if (bx == ebx && by == eby) {
                    nbx = bx;
                    nby = by;
                } else {
                    if (nbx < 0 || nbx >= h || nby < 0 || nby >= w) continue;
                    if (bvisited[nbx][nby] == 1) continue;
                }
                
                if (nrx == nbx && nry == nby) continue;
                if (nrx == bx && nry == by && nbx == rx && nby == ry) continue;
                
                rvisited[nrx][nry] = 1;
                bvisited[nbx][nby] = 1;
                // System.out.println(" " + nrx + nry + " " + nbx + nby);
                dfs(nrx, nry, nbx, nby, turn + 1);
                rvisited[nrx][nry] = 0;
                bvisited[nbx][nby] = 0;
            }
        }
    }
    
}