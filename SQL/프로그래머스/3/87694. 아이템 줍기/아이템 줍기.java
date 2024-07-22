class Solution {
    
    static int[][] visited = new int[101][101];
    static int[][] map = new int[101][101];
    
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};
    
    static Node[] queue = new Node[20000];
        
    class Node {
        int x;
        int y;
        
        Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    
    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        int answer = 0;
        
        for (int i = 0; i < 101; i++) {
            for (int j = 0; j < 101; j++) {
                visited[i][j] = 0;
                map[i][j] = 0;
                map[i][j] = 0;
            }
        }
        
        for (int[] single: rectangle) {
            for (int w = single[0] * 2; w <= single[2] * 2; w++) {
                for (int h = single[1] * 2; h <= single[3] * 2; h++) {
                    if (w == single[0] * 2 || w == single[2] * 2 || h == single[1] * 2 || h == single[3] * 2) {
                        if (map[h][w] == 2) continue;
                        map[h][w] = 1;
                    } else {
                        map[h][w] = 2;
                    }
                }
            }   
        }
        
        int front = 0;
        int rear = 0;
        
        queue[rear++] = new Node(characterY * 2, characterX * 2);
        queue[rear++] = new Node(characterY * 2, characterX * 2);
        
        visited[characterY * 2][characterX * 2] = 1;
        
        while (front < rear) {
            Node node = queue[front++];
            // System.out.println(node.x + " " + node.y);
            
            for (int k = 0; k < 4; k++) {
                int nx = node.x + dx[k];
                int ny = node.y + dy[k];
                
                if (nx > 100 || ny > 100) continue;
                
                if (nx >= 0 && ny >= 0 && map[nx][ny] == 1 && visited[nx][ny] == 0) {
                    visited[nx][ny] += visited[node.x][node.y] + 1;
                    queue[rear++] = new Node(nx, ny);
                }
            }
        }
        
        System.out.println(visited[itemY * 2][itemX * 2]);
        answer = visited[itemY * 2][itemX * 2] / 2;
        
        for (int i = 0; i < 21; i++) {
            for (int j = 0; j < 21; j++) {
                if (map[i][j] == 1) {
                    // System.out.print(0);
                } else {
                    // System.out.print(1);
                }
                // System.out.print(1);
            }
            // System.out.println();
        }
        
        return answer;
    }
}