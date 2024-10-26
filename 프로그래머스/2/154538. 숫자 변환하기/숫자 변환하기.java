import java.util.*;

class Solution {
    public int solution(int x, int y, int n) {
        int answer = 0;
        
        int[] numbers = new int[y + 1];
        
        int oper1 = x + n;
        int oper2 = x * 2;
        int oper3 = x * 3;
        
        numbers[x] = 1;
        
        Queue<Integer> queue = new LinkedList<>();
        queue.add(x);
        
        int nx;
        
        while (!queue.isEmpty()) {
            int cx = queue.poll();
            
            if (cx == y) break;
            
            nx = cx + n;
            
            if (nx <= y && numbers[nx] == 0) {
                queue.add(nx);
                numbers[nx] = numbers[cx] + 1;
            }
            
            nx = cx * 2;
            
            if (nx <= y && numbers[nx] == 0) {
                queue.add(nx);
                numbers[nx] = numbers[cx] + 1;
            }
            
            nx = cx * 3;
            
            if (nx <= y && numbers[nx] == 0) {
                queue.add(nx);
                numbers[nx] = numbers[cx] + 1;
            }
        }
        
        answer = numbers[y] - 1;
        
        return answer;
    }
}