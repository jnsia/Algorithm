import java.util.*;

class Solution {
    public int[] solution(int n, int[][] roads, int[] sources, int destination) {
        int[] answer = new int[sources.length];
        
        List<List<Integer>> matrix = new ArrayList<>();
        
        for (int i = 0; i < n + 1; i++) {
            matrix.add(new ArrayList<Integer>());
        }
        
        System.out.println(matrix.size());
        
        for (int[] road: roads) {
            int x = road[0];
            int y = road[1];
            
            matrix.get(x).add(y);
            matrix.get(y).add(x);
        }
        
        int[] visited = bfs(matrix, n, destination);
        
        for (int i = 0; i < sources.length; i++) {
            answer[i] = visited[sources[i]];
        }
        
        return answer;
    }
    
    private int[] bfs(List<List<Integer>> matrix, int n, int destination) {
        int[] visited = new int[n + 1];
        
        for (int i = 0; i < n + 1; i++) {
            visited[i] = -1;
        }
        
        visited[destination] = 0;
        
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(destination);
        
        while (!queue.isEmpty()) {
            int node = queue.poll();
            
            for (int nextNode: matrix.get(node)) {
                if (visited[nextNode] == -1) {
                    visited[nextNode] = visited[node] + 1;
                    queue.offer(nextNode);
                }
            }
        }
        
        return visited;
    }
}