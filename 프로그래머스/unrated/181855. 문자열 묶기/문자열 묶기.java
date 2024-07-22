class Solution {
    public int solution(String[] strArr) {
        int answer = 0;
        int[] cnt_arr = new int[31];
        int tmp_len;
        
        for (String tmp: strArr) {
            tmp_len = tmp.length();
            cnt_arr[tmp_len] += 1;
        }
        
        for (int i: cnt_arr) {
            System.out.println(i);
            
            if (i > answer) {
                answer = i;
            }
        }
        
        return answer;
    }
}