class Solution {
    public String solution(String my_string, int s, int e) {
        String answer = "";
        String tmp_str = "";
        
        for (int i = s; i <= e; i++) {
			tmp_str = my_string.charAt(i) + tmp_str;
		}
        
        System.out.println(tmp_str);
        
        for (int i = 0; i < my_string.length(); i++) {
			if (i >= s && i <= e) {
				answer += tmp_str.charAt(i - s);
			} else {
				answer += my_string.charAt(i);
			}
		}
        
        return answer;
    }
}