class Solution {
    public String[] solution(String[] strArr) {
        String[] result = new String[1001];
        int rear = 0;
        
        for (String tmp: strArr) {
            if (tmp.indexOf("ad") == -1) {
                result[rear++] = tmp;
            }
        }
        
        String[] answer = new String[rear];
        
        for (int i = 0; i < rear; i++) {
            answer[i] = result[i];
        }
        
        return answer;
    }
}