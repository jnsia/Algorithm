import java.util.*;

class Solution {
    public int solution(int[] order) {
        int answer = 0;
        
        List<Integer> stack = new ArrayList<>();
        
        int orderIndex = 0;
        
        for (int i = 1; i < order.length + 1; i++) {
            if (order[orderIndex] == i) {
                answer++;
                orderIndex++;
                
                while (stack.size() > 0) {
                    if (stack.get(stack.size() - 1) == order[orderIndex]) {
                        stack.remove(stack.size() - 1);
                        answer++; 
                        orderIndex++;
                    } else break;
                }
            } else {
                stack.add(i);            
            }
        }
        
        while (stack.size() > 0) {
            if (stack.get(stack.size() - 1) == order[orderIndex]) {
                stack.remove(stack.size() - 1);
                answer++; 
                orderIndex++;
            } else break;
        }
        
        return answer;
    }
}