import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        
        for (int score: scoville) {
            pq.add(score);
        }
        
        int first, second, result;
        
        while (pq.size() > 1) {
            first = pq.remove();
            second = pq.remove();
            
            result = first + (second * 2);
            
            if (first < K) {
                pq.add(result);
                answer++;
            }
            
            if (first >= K) break;
        }
        
        if (pq.size() > 0 && pq.remove() < K) answer = -1;
        
        return answer;
    }
}