import java.util.*;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        
        List<String> cacheArray = new ArrayList<>();
        
        for (String tempCity: cities) {
            Boolean isExist = false;
            
            String city = tempCity.toUpperCase();
            
            for (String cache: cacheArray) {
                if (cache.equals(city)) {
                    isExist = true;
                    break;
                }
            }
            
            if (isExist) {
                answer += 1;
                cacheArray.remove(city);
                cacheArray.add(city);
            } else {
                if (cacheSize == 0) {
                    answer += 5;
                    continue;
                }
                
                if (cacheArray.size() < cacheSize) {
                    cacheArray.add(city);
                } else {
                    cacheArray.remove(0);
                    cacheArray.add(city);
                }
                
                answer += 5;
            }
        }
        
        return answer;
    }
}