class Solution {
    public int[] solution(int[] num_list, int n) {
        int[] answer = new int[(int)(num_list.length - 1) / n + 1];
        
        for (int i = 0; i < num_list.length; i += n) {
            answer[(int)(i / n)] = num_list[i];
        }
        
        return answer;
    }
}