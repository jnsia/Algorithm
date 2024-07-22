class Solution {
    public String solution(String[] my_strings, int[][] parts) {
        String answer = "";
        int s, e;
        
        for (int i = 0; i < parts.length; i++) {
			s = parts[i][0];
			e = parts[i][1];
			
			for (int j = s; j <= e; j++) {
				answer += my_strings[i].charAt(j);
			}
		}
        
        return answer;
    }
}