import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        List<Integer> result = new ArrayList<>();
        
        for (int[] command: commands) {
            List<Integer> temp = new ArrayList<>();
            
            int i = command[0] - 1;
            int j = command[1];
            int k = command[2] - 1;
            
            for (int idx = i; idx < j; idx++) {
                temp.add(array[idx]);
            }
            
            temp.sort((x, y) -> (x - y));
            
            result.add(temp.get(k));
        }
        
        int[] answer = new int[result.size()];
        
        for (int idx = 0; idx < answer.length; idx++) {
            answer[idx] = result.get(idx);
        }
        
        return answer;
    }
}