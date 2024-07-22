class Solution {
    
    static Boolean[] existed = new Boolean[200001];
    
    public int solution(int[] nums) {
        int answer = 0;
        
        for (int i = 0; i < 200001; i++) {
            existed[i] = false;
        }
        
        for (int num: nums) {
            existed[num] = true;
        }
        
        for (int i = 0; i < 200001; i++) {
            if (existed[i]) {
                answer++;
            }
            
            if (answer == nums.length / 2) break;
        }
        
        return answer;
    }
}