import java.util.*;

class Solution {
    public int[] solution(String[] gems) {
        int[] answer = new int[2];

        Map<String, Integer> gemMap = new HashMap<>();
        Set<String> gemSet = new HashSet<>();
        
        for (String gem: gems) {
            gemMap.put(gem, 0);
            gemSet.add(gem);
        }
        
        int i = 0;
        int j = 0;
        
        int maxTypeNum = gemSet.size();
        gemSet.clear();
        
        int minLength = gems.length + 1;
        
        while (i < gems.length) {
            if (j == gems.length) {
                if (gemSet.size() == maxTypeNum && minLength > j - i) {
                    minLength = j - i;
                    answer[0] = i + 1;
                    answer[1] = j;
                }
                
                String gem = gems[i];
                int gemNum = gemMap.get(gem) - 1;
                gemMap.put(gem, gemNum);
                
                if (gemNum == 0) {
                    gemSet.remove(gem);
                }
                
                i++;
                continue;
            }
            
            if (gemSet.size() == maxTypeNum) {
                if (minLength > j - i) {
                    minLength = j - i;
                    answer[0] = i + 1;
                    answer[1] = j;
                }
                
                String gem = gems[i];
                int gemNum = gemMap.get(gem) - 1;
                gemMap.put(gem, gemNum);
                
                if (gemNum == 0) {
                    gemSet.remove(gem);
                }
                
                i++;
            } else {
                String gem = gems[j];
                int gemNum = gemMap.get(gem) + 1;
                gemMap.put(gem, gemNum);
                
                if (gemNum == 1) {
                    gemSet.add(gem);
                }
                
                j++;
            }
        }
        
        return answer;
    }
}