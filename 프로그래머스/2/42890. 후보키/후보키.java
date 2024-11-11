import java.util.*;

class Solution {
    
    static List<String> list = new ArrayList<>();
    
    public int solution(String[][] relation) {
        int answer = 0;
        
        int columnLength = relation[0].length;
        int[] bits = new int[columnLength];
        
        recursion(0, columnLength, bits, relation);
        
        for (int i = 0; i < list.size(); i++) {
            Boolean flag = true;
            int bit1 = Integer.parseInt(list.get(i), 2);
            
            for (int j = 0; j < list.size(); j++) {
                if (i == j) continue;
                int bit2 = Integer.parseInt(list.get(j), 2);
                // System.out.println(list.get(i) + " " + list.get(j) + " " + (bit1 & bit2));
                
                if ((bit1 & bit2) == bit2) {
                    flag = false;
                    break;
                }
            }
            
            if (flag) {
                System.out.println(list.get(i));
                answer++;
            }
        }
        
        return answer;
    }
    
    private void recursion(int index, int columnLength, int[] bits, String[][] relation) {
        if (index == columnLength) {
            validation(bits, relation);
            return;
        }
        
        bits[index] = 0;
        recursion(index + 1, columnLength, bits, relation);
        bits[index] = 1;
        recursion(index + 1, columnLength, bits, relation);
    }
    
    private void validation(int[] bits, String[][] relation) {
        Set<String> set = new HashSet();
        
        for (String[] rel: relation) {
            String word = "";
            
            for (int i = 0; i < bits.length; i++) {
                if (bits[i] == 0) continue;
                word += rel[i];
            }
            
            set.add(word);
            // System.out.println(word);
        }
        
        if (set.size() == relation.length) {
            String result = "";
            
            for (int bit: bits) {
                result += bit;
            }
            
            list.add(result);
        }
    }
}