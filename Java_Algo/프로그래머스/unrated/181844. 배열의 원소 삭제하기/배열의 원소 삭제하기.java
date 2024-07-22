import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[] delete_list) {
        List<Integer> answer = new ArrayList<>();
        
        for (int elem: arr) {
            boolean pass = false;
            for (int delete: delete_list) {
                if (elem == delete) {
                    pass = true;
                    break;
                }
            }
            
            if (!pass) {
                answer.add(elem);
            }
        }
        
        return answer.stream().mapToInt(x -> x).toArray();
    }
}