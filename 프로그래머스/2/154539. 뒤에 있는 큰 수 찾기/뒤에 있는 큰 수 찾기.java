import java.util.*;

class Solution {
    class Node {
        int index;
        int number;
        
        Node(int index, int number) {
            this.index = index;
            this.number = number;
        }
    }
    
    public int[] solution(int[] numbers) {
        int[] answer = new int[numbers.length];
        
        List<Node> stack = new ArrayList<>();
        
        for (int i = 0; i < numbers.length; i++) {
            int number = numbers[i];
            
            while (!stack.isEmpty()) {
                Node prev = stack.get(stack.size() - 1);
                
                if (prev.number < number) {
                    answer[prev.index] = number;
                    stack.remove(stack.size() - 1);
                } else {
                    break;
                }
            }
            
            stack.add(new Node(i, number));
        }
        
        while (!stack.isEmpty()) {
            Node node = stack.get(stack.size() - 1);
            answer[node.index] = -1;
            stack.remove(stack.size() - 1);
        }
        
        return answer;
    }
}