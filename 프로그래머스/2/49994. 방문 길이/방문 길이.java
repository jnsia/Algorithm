class Solution {
    public int solution(String dirs) {
        int answer = 0;
        
        int[][][] map = new int[11][11][4];
        
        int x = 5;
        int y = 5;
        
        for (int i = 0; i < dirs.length(); i++) {
            char dir = dirs.charAt(i);
            int step = -1;
            
            int nx = x;
            int ny = y;
            
            if (dir == 'U') {
                step = 0;
                nx -= 1;
            }
            
            if (dir == 'D') {
                step = 2;
                nx += 1;
            }
            
            if (dir == 'L') {
                step = 1;
                ny -= 1;
            }
            
            if (dir == 'R') {
                step = 3;
                ny += 1;
            }
            
            if (nx < 0 || nx >= 11 || ny < 0 || ny >= 11) continue;
            
            if (map[x][y][step] == 0 && map[nx][ny][(step + 2) % 4] == 0) {
                answer++;
                map[x][y][step] = 1;
                map[nx][ny][(step + 2) % 4] = 1;
            }
            
            x = nx;
            y = ny;
        }
        
        return answer;
    }
}