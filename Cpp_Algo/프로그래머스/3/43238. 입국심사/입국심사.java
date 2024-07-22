import java.lang.Math;

class Solution {
    
    static long MAX = 1000000001 * 1000000001l;
    
    public long solution(int n, int[] times) {
        long answer = 0;
        
        answer = lowerBound(n, times);
        
        return answer;
    }
    
    public long check(long mid, int[] times) {
        long sum = 0;
        
        for (int time: times) {
            sum += mid / time;
        }
        
        return sum;
    }
    
    public long lowerBound(int n, int[] times) {
        long low = 0;
        long high = MAX;
        long minValue = high;
        
        while (low <= high) {
            long mid = (low + high) / 2;
            long result = check(mid, times);
            
            if (result == n) {
                high = mid - 1;
                minValue = Math.min(minValue, mid);
            } else if (result > n) {
                high = mid - 1;
                minValue = Math.min(minValue, mid);
            } else {
                low = mid + 1;
            }
        }
        
        return minValue;
    }
}