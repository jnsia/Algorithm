import java.util.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        List<Integer> list = new ArrayList<>();
        
        for (int num: arr) {
            if (num % divisor == 0) list.add(num);
        }
        
        Collections.sort(list);
        
        int[] answer = new int[list.size()];

        for (int i = 0; i < answer.length; i++) {
            answer[i] = list.get(i);
        }
        
        if (answer.length == 0) answer = new int[] {-1};
        
        return answer;
    }
}