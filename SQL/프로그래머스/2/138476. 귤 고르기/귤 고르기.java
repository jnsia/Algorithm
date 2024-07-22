import java.util.*;

class Solution {
    
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        int[] counting = new int[10000001];
        
        for (int t: tangerine) {
            counting[t] += 1;
        }
        
        List<Integer> arr = new ArrayList<>();
        
        for (int c: counting) {
            if (c > 0) arr.add(c);
        }
        
        Collections.sort(arr, (a, b) -> (b - a));
        
        int i = 0;
        
        while (k > 0) {
            k -= arr.get(i);
            i++;
            answer++;
        }
        System.out.println(arr.get(0));
        
        return answer;
    }
}