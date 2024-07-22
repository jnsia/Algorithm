class Solution {
    public int solution(String number) {
        int answer = 0;
        int res = 0;
        char tmp;
        
        for (int i = 0; i < number.length(); i++) {
            tmp = number.charAt(i);
            res += tmp - '0';
        }
        
        answer = res % 9;
        
        return answer;
    }
}