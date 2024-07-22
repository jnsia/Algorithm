import java.lang.Math;

class Solution {
    
    class Node {
        int data;
        int type;
        
        Node () {
            this.data = 0;
            this.type = 0;
        }
        
        Node (int data, int type) {
            this.data = data;
            this.type = type;
        }
    }
    
    static Node[] queue = new Node[200001];
    static Boolean[][] graph = new Boolean[101][101];
    
    public int solution(int n, int[][] wires) {
        int answer = 201;
        
        for (int i = 0; i < 101; i++) {
            for (int j = 0; j < 101; j++) {
                graph[i][j] = false;
            }
        }
        
        for (int[] wire: wires) {
            int start = wire[0];
            int end = wire[1];
            
            graph[start][end] = true;
            graph[end][start] = true;
        }
        
        for (int i = 0; i < 101; i++) {
            queue[i] = new Node();
        }
        
        for (int[] wire: wires) {
            int f1 = wire[0];
            int f2 = wire[1];
            
            int result = bfs(n, f1, f2);
            
            answer = Math.min(answer, result);
        }
        
        return answer;
    }
    
    public int bfs(int n, int f1, int f2) {
        Boolean[] visited = new Boolean[101];
        
        for (int i = 1; i < 101; i++) {
            queue[i] = new Node();
            visited[i] = false;
        }
        
        int rf1 = 1;
        int rf2 = 1;
        
        visited[f1] = true;
        visited[f2] = true;
        
        int front = 0;
        int rear = 0;
        
        queue[rear++] = new Node(f1, 1);
        queue[rear++] = new Node(f2, 2);
        
        while (front != rear) {
            Node node = queue[front++];
            
            for (int i = 1; i < n + 1; i++) {
                if (graph[node.data][i] && !visited[i]) {
                    Node nextNode = new Node(i, node.type);
                    // System.out.println(nextNode.data);
                    queue[rear++] = nextNode;
                    visited[i] = true;
                    
                    if (node.type == 1) rf1++;
                    else rf2++;
                }
            }
        }
        
        return Math.abs(rf1 - rf2);
    }
    
}