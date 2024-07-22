import java.lang.Math;

class Solution {
    
    static int[] visited = new int[9];
    static int status = 0;
    
    public int solution(int k, int[][] dungeons) {
        int answer = -1;
        
        dfs(dungeons, k, 0);
        
        if (status > 0) {
            answer = status;
        }
        
        return answer;
    }
    
    public void dfs(int[][] dungeons, int currentK, int result) {
        status = Math.max(result, status);
                                                                 
        if (currentK < 0) {
            status = Math.max(result, status);
            System.out.println(result);
            return;
        }
        
        for (int i = 0; i < dungeons.length; i++) {
            if (visited[i] == 0 && currentK - dungeons[i][0] >= 0) {
                visited[i] = 1;
                dfs(dungeons, currentK - dungeons[i][1], result + 1);
                visited[i] = 0;
            }
        }
        
    }
}