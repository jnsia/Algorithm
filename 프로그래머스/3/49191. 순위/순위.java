class Solution {
    public int solution(int n, int[][] results) {
        int answer = 0;
        
        int[][] graph = new int[n + 1][n + 1];
        
        for (int[] result: results) {
            int win = result[0];
            int lose = result[1];
            
            graph[win][lose] = 1;
            graph[lose][win] = -1;
        }
        
        for (int i = 1; i <= n; i++) {
            int winNumber = bfs(n, i, graph, 1);
            int loseNumber = bfs(n, i, graph, -1);
            
            System.out.println(winNumber + " " + loseNumber);
            
            if (winNumber + loseNumber == n + 1) answer++;
        }
        
        return answer;
    }
    
    private int bfs(int n, int node, int[][] graph, int type) {        
        int[] visited = new int[n + 1];
        visited[node] = 1;
        
        int front = 0;
        int rear = 0;
        int[] queue = new int[5000];
        
        queue[rear++] = node;
        
        while (front < rear) {
            int curr = queue[front++];
            
            for (int next = 1; next <= n; next++) {
                if (graph[curr][next] == type && visited[next] == 0) {
                    visited[next] = 1;
                    queue[rear++] = next;
                }
            }
        }
        
        int result = 0;
        
        for (int i = 1; i <= n; i++) {
            if (visited[i] == 1) result++;
        }
        
        return result;
    }
}