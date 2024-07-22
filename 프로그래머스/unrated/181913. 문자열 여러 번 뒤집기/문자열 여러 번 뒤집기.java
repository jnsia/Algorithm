class Solution {
    public String solution(String my_string, int[][] queries) {
        String answer = "";
        char[] result = new char[my_string.length()];
        int s, e;
        
        for (int i = 0; i < result.length; i++) {
			result[i] = my_string.charAt(i);
		}
        
        for (int i = 0; i < queries.length; i++) {
			s = queries[i][0];
			e = queries[i][1];
			
			char[] tmp_arr = new char[e - s + 1];
			
			for (int j = s; j <= e; j++) {
				tmp_arr[j - s] = result[e - j + s];
			}
			
			for (int k = s; k <= e; k++) {
				result[k] = tmp_arr[k - s];
			}
		}
        
        for (char word: result) {
            answer += word;
        }
        
        return answer;
    }
}