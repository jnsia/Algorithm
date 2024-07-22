class Solution {
    
    class Truck {
        int weight;
        int time;
        
        Truck(int weight, int time) {
            this.weight = weight;
            this.time = time;
        }
    }
    
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        
        int index = 0;
        int front = 0;
        int rear = 0;
        Truck[] queue = new Truck[10001];
        int time = 0;
        int currentWeight = 0;
        
        while (front < rear || index < truck_weights.length) {
            while (front < rear) {
                if (time - queue[front].time >= bridge_length) {
                    // System.out.println(time + " " + queue[front].time);
                    currentWeight -= queue[front].weight;
                    // System.out.println(time + " " + currentWeight);
                    front++;
                } else break;
            }
            
            if (index < truck_weights.length && rear - front < bridge_length && currentWeight + truck_weights[index] <= weight) {
                currentWeight += truck_weights[index];
                queue[rear++] = new Truck(truck_weights[index], time);
                // System.out.println(time + " " + index + " " + currentWeight);
                index++;
            }
            
            // if (front == rear && index > truck_weights.length) break;
            
            time++;
        }
        
        answer = time;
        
        return answer;
    }
}