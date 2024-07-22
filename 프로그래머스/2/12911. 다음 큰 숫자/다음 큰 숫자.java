class Solution {
    public int solution(int n) {
        int answer = 0;
        int nBinaryOne = binaryOne(n);
        
        for (int i = n + 1; i < 1000001; i++) {
            if (nBinaryOne == binaryOne(i)) {
                answer = i;
                break;
            }
        }
        
        return answer;
    }
    
    private int binaryOne(int number) {
        int result = 0;
        
        while (number > 0) {
            if (number % 2 == 1) {
                result++;
            }
            
            number /= 2;
        }
        
        return result;
    }
}