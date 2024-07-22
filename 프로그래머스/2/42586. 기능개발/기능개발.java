class Solution {
    
    class Node {
        int index;
        int progress;
        
        Node (int index, int progress) {
            this.index = index;
            this.progress = progress;
        }
    }
    
    public int[] solution(int[] progresses, int[] speeds) {
        int[] answer = new int[101];
        Node[] queue = new Node[100001];
        int[] completed = new int[101];
        
        completed[0] = 1;
        
        int front = 0;
        int rear = 0;
        
        int size = 0;
        
        for (int i = 1; i < speeds.length + 1; i++) {
            queue[rear++] = new Node(i, progresses[i - 1]);
        }
        
        int time = 0;
        
        while (front < rear) {
            int rest = rear - front;
            int temp = 0;
            
            for (int i = 0; i < rest; i++) {
                Node node = queue[front++];
                int nextProgress = node.progress + speeds[node.index - 1];
                
                if (completed[node.index - 1] == 1 && nextProgress >= 100) {
                    temp += 1;
                    completed[node.index] = 1;
                } else {
                    queue[rear++] = new Node(node.index, nextProgress);
                }
            }
            
            if (temp > 0) {
                answer[size++] = temp;
            }
        }
        
        int[] result = new int[size];
        
        for (int i = 0; i < size; i++) {
            result[i] = answer[i];
        }
        
        return result;
    }
}