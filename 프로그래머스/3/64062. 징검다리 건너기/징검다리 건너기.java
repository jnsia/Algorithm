class Solution {
    public int solution(int[] stones, int k) {
        int answer = 0;
        
        answer = binarySearch(stones, k);
        
        return answer;
    }
    
    private int binarySearch(int[] stones, int k) {
        int result = 0;
        
        int low = 0;
        int high = 200000001;
        
        while (low <= high) {
            int mid = (low + high) / 2;
            
            if (isSuccess(stones, mid, k)) {
                low = mid + 1;
                result = Math.max(result, mid);
            } else {
                high = mid - 1;
            }
        }
        
        return result;
    }
    
    private Boolean isSuccess(int[] stones, int number, int k) {
        Boolean result = true;
        int count = 0;
        
        for (int stone: stones) {
            if (number > stone) {
                count++;
            } else {
                count = 0;
            }
            
            if (count >= k) {
                result = false;
                break;
            }
        }
        
        return result;
    }
}