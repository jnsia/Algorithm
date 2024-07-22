import java.util.*;

class Solution {
    public String[] solution(String my_string) {
        List<String> result = new ArrayList<String>();
        int len = my_string.length();
        
        for (int i = 0; i < len; i++) {
        	String tmp = "";
        	
			for (int j = len - 1; j >= len - i - 1; j--) {
				tmp = my_string.charAt(j) + tmp;
			}
			
			result.add(tmp);
		}
        
    	String[] answer = new String[result.size()];
        
    	int size = 0;
    	
    	for (String temp : result) {
			answer[size++] = temp;
		}
    	
        Arrays.sort(answer);
        
        return answer;
    }
}