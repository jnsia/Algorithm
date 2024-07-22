import java.util.*;

class Solution {
    public int[][] solution(int n) {
        int[][] answer = new int[n][n];
        int[] dx = {0, 1, 0, -1};
        int[] dy = {1, 0, -1, 0};
        int num = 1;
        int direction = 0;
        int[][] queue = new int[n * n * n + 1][3];
        int rear = 0;
        int x, y, z, nx, ny, nz;
        answer[0][0] = num++;
        
        while (rear < n * n * n) {
            
            x = queue[rear][0];
            y = queue[rear][1];
            z = queue[rear][2];
        
            if (rear != 0 && x == 0 && y == 0) {
                break;
            }
            
            nx = x + dx[z];
            ny = y + dy[z];
            nz = (z + 1) % 4;
            
            rear++; 
            
            if ((nx >= 0 && nx < n) && (ny >= 0 && ny < n) && (answer[nx][ny] == 0)) {
                answer[nx][ny] = num++;
                queue[rear][0] = nx;
                queue[rear][1] = ny;
                queue[rear][2] = z;
            } else {
                queue[rear][0] = x;
                queue[rear][1] = y;
                queue[rear][2] = nz;
            }  
        }

        return answer;
    }
}