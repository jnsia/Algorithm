import java.util.*;

class Solution {
    public long solution(long n) {
        long answer = 0;
        
        String str = n + "";
        char[] arr = new char[str.length()];
        
        for (int i = 0; i < str.length(); i++) {
            arr[i] = str.charAt(i);
        }
        
        Arrays.sort(arr);
        
        String result = "";
        
        for (int i = 0; i < str.length(); i++) {
            result = arr[i] + result;
        }
        
        answer = Long.parseLong(result);
        
        return answer;
    }
}