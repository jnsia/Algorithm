import java.util.Arrays;

class Solution {
    public int solution(int[] arr) {
        int answer = 0;
        int size;
        int[] tmp_arr = new int[arr.length];
        
        for (int x = 0; x < arr.length; x++) {
            size = 0;
                        
            for (int y = 0; y < arr.length; y++) {
                tmp_arr[y] = arr[y];
            }
            
            for (int num: arr) {
                if (num >= 50 && num % 2 == 0) {
                    arr[size] = num / 2;
                } else if (num < 50 && num % 2 == 1) {
                    arr[size] = num * 2 + 1;
                }
                
                size++;
            }
            
            if (Arrays.toString(arr).equals(Arrays.toString(tmp_arr))) {
                answer = x;
                break;
            }

        }
        
        
        return answer;
    }
}