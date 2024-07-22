class Solution {
    public String[] solution(String[] str_list) {
        String[] answer = {};
        
        int front = -1;
        int rear = -1;

        for (int i = 0; i < str_list.length; i++) {
            if (str_list[i].equals("l")) {
                rear = i;
                break;
            }
            
            if (str_list[i].equals("r")) {
                front = i;
                break;
            }
        }
        
        if (front >= 0) {
            String[] res_arr = new String[str_list.length - front - 1];
            
            for (int i = front; i < str_list.length - 1; i++) {
                res_arr[i - front] = str_list[i + 1];
            }
            
            answer = res_arr;
        } else if (rear >= 0) {
            String[] res_arr = new String[rear];
            
            for (int i = 0; i < rear; i++) {
                res_arr[i] = str_list[i];
            }
            
            answer = res_arr;
        }
        
        return answer;
    }
}