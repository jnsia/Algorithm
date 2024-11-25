import java.util.*;

class Solution {
    
    class Node {
        int index;
        double number;
        
        Node(int index, double number) {
            this.index = index;
            this.number = number;
        }
    }
    
    public int[] solution(int N, int[] stages) {
        int[] answer = new int[N];
        
        double[] count = new double[N + 2];
        int people = stages.length;
        
        for (int stage: stages) {
            count[stage]++;
        }
        
        int index = 1;
        List<Node> array = new ArrayList<>();
        
        while (index < N + 1) {
            double number = count[index];
            array.add(new Node(index, number / people));
            people -= number;
            index++;
        }
        
        Collections.sort(array, new Comparator<Node>() {
            public int compare(Node node1, Node node2) {
                if (node1.number < node2.number) {
                    return 1;
                } else if (node1.number > node2.number) {
                    return -1;
                } else {
                    return 0;
                }
            }
        });
        
        index = 0;
        
        for (Node node: array) {
            answer[index++] = node.index;
            // System.out.println(node.index + " " + node.number);
        }
        
        return answer;
    }
}