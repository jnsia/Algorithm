import java.util.*;
import java.lang.Math;

class Solution {
    
    public int solution(int distance, int[] rocks, int n) {
        int answer = 0;
        
        Arrays.sort(rocks);
        answer = binarySearch(0, distance, rocks, n);
        
        return answer;
    }
    
    private int binarySearch(int start, int end, int[] rocks, int chance) {
        int low = start;
        int high = end;
        
        int result = 0;
        
        while (low <= high) {
            int mid = (low + high) / 2;
            
            if (canPass(start, end, rocks, chance, mid)) {
                result = Math.max(result, mid);
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        
        return result;
    }
    
    private Boolean canPass(int start, int end, int[] rocks, int chance, int distance) {
        Boolean result = true;
        
        int current = start;
        
        for (int rock: rocks) {
            int diff = rock - current;
            
            if (diff < distance) {
                if (chance > 0) {
                    chance--;
                    continue;
                } else {
                    result = false;
                    break;
                }
            }
            
            current = rock;
        }
        
        if (end - current < distance) {
            if (chance <= 0) {
                result = false;
            }
        }
        
        return result;
    }
    
}