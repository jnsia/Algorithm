import java.util.*;

class Solution {
    class Node {
        int x;
        int y;
        int d;
        
        Node(int x, int y, int d) {
            this.x = x;
            this.y = y;
            this.d = d;
        }
    }
    
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};
    
    public int solution(int[][] board) {
        int answer = 0;
        
        int N = board.length;
        
        answer = bfs(N, board);
        
        return answer;
    }
    
    private int bfs(int N, int[][] board) {
        int[][][] visited = new int[N][N][4];
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < 4; k++) {
                    if (i == 0 && j == 0) {
                        visited[i][j][k] = 0;
                    } else {
                        visited[i][j][k] = N * N * 600;
                    }
                }
            }
        }
        
        Queue<Node> queue = new LinkedList<>();
        
        queue.add(new Node(0, 0, 0));
        queue.add(new Node(0, 0, 1));
        
        while (!queue.isEmpty()) {
            Node node = queue.poll();
            // System.out.println(node.x + " " + node.y + " " + node.d);
            
            for (int i = 0; i < 4; i++) {
                int nx = node.x + dx[i];
                int ny = node.y + dy[i];
                
                if (nx == 0 && ny == 0) continue;
                if (nx < 0 || nx >= N) continue;
                if (ny < 0 || ny >= N) continue;
                if (board[nx][ny] == 1) continue;
                
                if (node.d == i) {
                    if (visited[nx][ny][node.d] > visited[node.x][node.y][node.d] + 100) {
                        visited[nx][ny][node.d] = visited[node.x][node.y][node.d] + 100;
                        queue.add(new Node(nx, ny, node.d));
                    }
                } else {
                    if (visited[nx][ny][i] > visited[node.x][node.y][node.d] + 600) {
                        visited[nx][ny][i] = visited[node.x][node.y][node.d] + 600;
                        queue.add(new Node(nx, ny, i));
                    }
                }
            }
        }
        
        int result = N * N * 600;
        
        for (int i = 0; i < 4; i++) {
            result = Math.min(result, visited[N - 1][N - 1][i]);
        }
        
        return result;
    }
}