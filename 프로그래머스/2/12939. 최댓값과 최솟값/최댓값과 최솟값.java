import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
    
        List<Integer> arr = new ArrayList<>();
        
        for (String word: s.split(" ")) {
            System.out.println(word);
            arr.add( Integer.parseInt(word) );
        }
        
        Collections.sort(arr);
        
        answer += arr.get(0) + " " + arr.get(arr.size() - 1);
        
        return answer;
    }
}