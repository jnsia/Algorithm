class Solution {
    class Node {
        int x;
        int y;
        
        Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    
    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, 1, 0, -1};
    
    static int[][] visited = new int[101][101];
    static Node[] queue = new Node[10001];
    
    public int solution(int[][] maps) {
        int answer = 0;
        
        int h = maps.length;
        int w = maps[0].length;
        
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                if (maps[i][j] == 0) {
                    visited[i][j] = -1;
                } else {
                    visited[i][j] = 0;
                }
            }
        }
        
        int front = 0;
        int rear = 0;
        
        queue[rear++] = new Node(0, 0);
        visited[0][0] = 1;
        
        while (front < rear) {
            Node node = queue[front++];
            
            for (int k = 0; k < 4; k++) {
                int nx = node.x + dx[k];
                int ny = node.y + dy[k];
                
                if (nx < 0 || nx >= h || ny < 0 || ny >= w) continue;
                
                if (visited[nx][ny] == 0) {
                    visited[nx][ny] = visited[node.x][node.y] + 1;
                    queue[rear++] = new Node(nx, ny);
                }
            }
        }
        
        answer = visited[h - 1][w - 1];
        
        if (answer == 0) {
            answer = -1;
        }
        
        return answer;
    }
}