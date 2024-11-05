import java.util.*;

class Solution {
    public int[] solution(String msg) {        
        int number = 1;
        
        Map<String, Integer> wordMap = new HashMap<>();
        
        for (int i = (int) 'A'; i <= (int) 'Z'; i++) {
            String word = (char) i + "";
            wordMap.put(word, number++);
        }
        
        List<Integer> results = new ArrayList<>();
        String input = "";
        
        for (int i = 0; i < msg.length(); i++) {
            char current = msg.charAt(i);
            input += current;
            
            if (i == msg.length() - 1) {
                results.add(wordMap.get(input));
                input = "";
            } else {
                char next = msg.charAt(i + 1);
                
                if (wordMap.get(input + next) == null) {
                    wordMap.put(input + next, number++);
                    // System.out.println(input);
                    results.add(wordMap.get(input));
                    input = "";
                }
            }
        }
        
        int[] answer = new int[results.size()];
        
        for (int i = 0; i < answer.length; i++) {
            answer[i] = results.get(i);
        }
        
        // System.out.println(results.toString());
        
        return answer;
    }
}