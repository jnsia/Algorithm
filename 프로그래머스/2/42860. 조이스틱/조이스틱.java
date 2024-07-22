class Solution {
    public int solution(String name) {
        int answer = 0;
        int len = name.length();
        int init = (int) 'A';

        int idx;
        int move = len - 1;

        for(int i = 0; i < name.length(); i++){
            int tmp = (int) name.charAt(i) - init;
            answer += Math.min(tmp, 26 - tmp);

            idx = i + 1;
            
            while (idx < len && name.charAt(idx) == 'A') idx++;

            move = Math.min(move, i * 2 + (len - idx));
            move = Math.min(move, (len - idx) * 2 + i);
        }
        
        return answer + move;
    }
}