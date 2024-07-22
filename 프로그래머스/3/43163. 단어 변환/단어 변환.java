import java.lang.Math;

class Solution {
    
    static int temp = 500;
    
    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        
        Boolean[] collected = new Boolean[words.length];
        
        for (int i = 0; i < words.length; i++) {
            collected[i] = false;
        }
        
        dfs(0, begin, target, words, collected);
        
        if (temp != 500) {
            answer = temp;
        }
        
        return answer;
    }
    
    private void dfs(int count, String result, String target, String[] words, Boolean[] collected) {
        if (result.equals(target)) {
            temp = Math.min(temp, count);
            return;        
        }
        
        for (int i = 0; i < words.length; i++) {
            if (collected[i] == false && canConvert(result, words[i])) {
                collected[i] = true;
                dfs(count + 1, words[i], target, words, collected);
                collected[i] = false;
            }
        }
        
        return;
    }
    
    private Boolean canConvert(String key, String word) {
        int numberOfDiffChar = 0;
        
        for (int i = 0; i < word.length(); i++) {
            if (key.charAt(i) != word.charAt(i)) {
                numberOfDiffChar++;
            }                
        }
        
        if (numberOfDiffChar == 1) {
            return true;
        } else {
            return false;
        }
    }
}