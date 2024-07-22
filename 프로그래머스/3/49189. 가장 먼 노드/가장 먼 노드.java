import java.util.*;
import java.lang.Math;

class Solution {
    
    static int[] queue = new int[10000000];
    static List<List<Integer>> graph = new ArrayList<>();
    
    public int solution(int n, int[][] edge) {
        int answer = 0;
        
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<Integer>());
        }
        
        for (int[] e: edge) {
            graph.get(e[0]).add(e[1]);
            graph.get(e[1]).add(e[0]);
        }
        
        int front = 0;
        int rear = 1;
        
        queue[0] = 1;
        
        int[] visited = new int[n + 1];
        
        visited[1] = 1;
        
        int max = 1;
        
        while (front < rear) {
            int node = queue[front++];
            
            for (int nextNode: graph.get(node)) {
                if (visited[nextNode] == 0) {
                    queue[rear++] = nextNode;
                    visited[nextNode] = visited[node] + 1;
                    max = Math.max(max, visited[nextNode]);
                }
            }
        }
        
        for (int v: visited) {
            if (v == max) answer++;
        }
        
        return answer;
    }
}