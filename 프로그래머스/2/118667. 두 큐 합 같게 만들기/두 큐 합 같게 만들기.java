import java.util.*;

class Solution {
    public int solution(int[] queue1, int[] queue2) {
        int answer = 0;
        
        long sum1 = 0;
        long sum2 = 0;
        
        Queue<Integer> q1 = new LinkedList<>();
        Queue<Integer> q2 = new LinkedList<>();
        
        for (int number: queue1) {
            q1.add(number);
            sum1 += number;
        }
        
        for (int number: queue2) {
            q2.add(number);
            sum2 += number;
        }
        
        System.out.println(sum1 + " " + sum2);
        while (!q1.isEmpty() && !q2.isEmpty() && sum1 != sum2) {
            if (answer > (queue1.length + queue2.length) * 2 + 1) {
                answer = -1;
                break;
            }
            
            if (sum1 < sum2) {
                int number = q2.poll();
                sum2 -= number;
                sum1 += number;
                q1.add(number);
            } else {
                int number = q1.poll();
                sum1 -= number;
                sum2 += number;
                q2.add(number);
            }
            
            // System.out.println(sum1 + " " + sum2);
            answer++;
        }
        
        if (q1.isEmpty() || q2.isEmpty()) answer = -1;
        
        return answer;
    }
}