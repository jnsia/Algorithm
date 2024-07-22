import java.util.Arrays;

class Solution {
    
    public int[] solution(int[] arr) {
        
        int n = 1;
        for(int i = 1; i <= 11; i++){
            if(arr.length <= n){
                return Arrays.copyOf(arr, n);
            }
            n *= 2;
        }
        return new int[0];
    }
}