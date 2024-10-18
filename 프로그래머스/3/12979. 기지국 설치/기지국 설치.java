class Solution {
    public int solution(int n, int[] stations, int w) {
        int answer = 0;
        
        int current = 1;
        int count = 0;
        int range = 2 * w + 1;
        
        for (int i = 0; i < stations.length; i++) {
            int start = stations[i] - w;
            int end = stations[i] + w;
            
            int term = start - current;
            current = end + 1;
            
            if (term <= 0) continue;
            
            count += (term - 1) / range + 1;
        }
        
        if (current <= n) {
            count += (n - current) / range + 1;
        }
        
        System.out.println(count);
        
        answer = binarySearch(n, count);

        return answer;
    }
    
    private int binarySearch(int n, int count) {
        int result = 200000001;
        
        int low = 0;
        int high = n;
        
        while (low <= high) {
            int mid = (low + high) / 2;
            
            if (count <= mid) {
                high = mid - 1;
                result = Math.min(result, mid);
            } else {
                low = mid + 1;
            }
        }
        
        return result;
    }
}