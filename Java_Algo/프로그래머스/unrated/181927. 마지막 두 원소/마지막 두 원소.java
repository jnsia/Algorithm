class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[num_list.length + 1];
        int a, b;
        
        for (int i = 0; i < num_list.length; i++) {
            answer[i] = num_list[i];
        }
        
        a = num_list[num_list.length - 1];
        b = num_list[num_list.length - 2];
        
        if (a > b) {
            answer[num_list.length] = a - b;
        } else {
            answer[num_list.length] = a * 2;
        }
        
        
        return answer;
    }
}