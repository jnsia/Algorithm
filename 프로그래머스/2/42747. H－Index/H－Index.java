import java.util.*;

class Solution {
    
    static int[] counting = new int[10001];
    
    public int solution(int[] citations) {
        int answer = 0;
        
        int total = citations.length;
        
        for (int citation: citations) {
            counting[citation] += 1;
        }
        
        for (int i = 9999; i >= 0; i--) {
            counting[i] += counting[i + 1];
        }
        
        for (int h = 0; h < 10001; h++) {
            int quotation = counting[h];
            
            if (quotation != 0) System.out.print(quotation + ",");
            
            if (quotation >= h && total - quotation <= h) {
                answer = h;            
            }
        }
        
        return answer;
    }    
}