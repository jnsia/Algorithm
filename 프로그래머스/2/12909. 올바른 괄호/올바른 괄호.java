class Solution {
    boolean solution(String s) {
        boolean answer = true;

        char[] stack = new char[100001];
        int top = 0;

        for (int i = 0; i < s.length(); i++) {
            char word = s.charAt(i);
            
            if (top == 0 && word == ')') {
                answer = false;
                break;
            }
            
            if (word == '(') {
                stack[top++] = '(';
            } else if (word == ')') {
                if (stack[top - 1] == '(') {
                    top--;
                } else if (stack[top - 1] == ')') {
                    answer = false;
                    break;
                }
                
            }
        }
        
        if (top > 0) answer = false;
        
        System.out.println("Hello Java");

        return answer;
    }
}