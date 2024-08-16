class Solution
{
    public int solution(String s)
    {
        int answer = -1;
        
        int index = 0;
        char[] stack = new char[1000001];
        
        for (int i = 0; i < s.length(); i++) {
            char word = s.charAt(i);
            
            if (index == 0) {
                stack[index++] = word;
            } else {
                if (stack[index - 1] == word) {
                    index -= 1;                    
                } else {
                    stack[index++] = word;                    
                }
            }
        }
        
        if (index == 0) answer = 1;
        else answer = 0;

        return answer;
    }
}