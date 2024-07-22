class Solution {
    class Node {
        int priority;
        int location;
        
        Node(int priority, int location) {
            this.priority = priority;
            this.location = location;
        }
    }
    
    public int solution(int[] priorities, int location) {
        int answer = 0;
        
        int[] countArray = new int[10];
        Node[] queue = new Node[10001];
        
        int front = 0;
        int rear = 0;
        int index = 0;
        
        for (int priority: priorities) {
            countArray[priority] += 1;
            queue[rear++] = new Node(priority, index);
            index++;
        }
        
        int execute = 0;
        int current = 9;
        
        while (front < rear) {
            while (countArray[current] == 0) {
                current--;
                System.out.println(current);
            }
            
            Node node = queue[front];
            
            if (node.priority == current) {
                execute++;
                
                if (node.location == location) {
                    answer = execute;
                }
                
                front++;
                countArray[node.priority] -= 1;
            } else {
                queue[rear] = node;
                rear++;
                front++;
            }
        }
        
        return answer;
    }
}