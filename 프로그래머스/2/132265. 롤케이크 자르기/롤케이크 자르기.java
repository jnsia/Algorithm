import java.util.*;

class Solution {
    public int solution(int[] topping) {
        int answer = 0;
        
        int toppingNumber1 = 0;
        int toppingNumber2 = 0;
        
        Map<Integer, Integer> topping1 = new HashMap<Integer, Integer>();
        Map<Integer, Integer> topping2 = new HashMap<Integer, Integer>();
        
        int index = 0;
        
        for (int topp: topping) {
            if (topping2.get(topp) == null) {
                toppingNumber2++;
            }
            
            topping1.put(topp, 0);
            topping2.put(topp, topping2.getOrDefault(topp, 0) + 1);
        }
        
        while (index < topping.length) {
            int topp = topping[index];
            
            if (topping1.get(topp) == 0) {
                toppingNumber1++;
            }
            
            topping1.put(topp, topping2.getOrDefault(topp, 0) + 1);
            topping2.put(topp, topping2.getOrDefault(topp, 0) - 1);
            
            if (topping2.get(topp) == 0) {
                toppingNumber2--;
            }
            
            if (toppingNumber1 == toppingNumber2) {
                answer++;
            }
            
            index++;
        }
        
        return answer;
    }
}