import java.util.PriorityQueue;

class Solution {
    public long solution(int n, int[] works) {
        long answer = 0;
        
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        
        for (int work: works) {
            pq.add(-work);
        }
        
        int p;
        
        while (pq.size() > 0 && n > 0) {
            p = pq.remove();
            
            if (p + 1 < 0) {
                pq.add(p + 1);
            }
            
            n--;
        }
        
        while (pq.size() > 0) {
            p = pq.remove();
            System.out.println(p);
            answer += p * p;
        }
        
        return answer;
    }
}