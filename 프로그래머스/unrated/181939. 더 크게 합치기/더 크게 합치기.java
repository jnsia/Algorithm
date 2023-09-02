class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        String a_str = Integer.toString(a);
        String b_str = Integer.toString(b);
        
        int apb = Integer.parseInt(a_str + b_str);
        int bpa = Integer.parseInt(b_str + a_str);
        
        if (apb >= bpa) {
            answer = apb;
        } else {
            answer = bpa;
        }
        
        return answer;
    }
}