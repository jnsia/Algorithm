class Solution {
    
    static String[] aeiou = {"A", "E", "I", "O", "U"};
    static int count = 0;
    static int answer = 0;
    
    public int solution(String word) {
        
        dfs(0, "", word);
        
        return answer;
    }
    
    private void dfs(int index, String result, String word) {
        if (index > 5) return;
        
        if (index > 0 && index <= 5) {
            count++;
            
            // System.out.println(result);
            if (result.equals(word)) {
                answer = count;
            }
        }
        
        for (int i = 0; i < 5; i++) {
            dfs(index + 1, result + aeiou[i], word);
        }
        
        return;
    }
}