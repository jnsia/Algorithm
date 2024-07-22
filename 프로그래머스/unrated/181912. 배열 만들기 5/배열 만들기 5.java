

import java.util.*;

class Solution {
    public int[] solution(String[] intStrs, int k, int s, int l) {
        List<Integer> answer = new ArrayList<>();
        String tmp;
        int num;
        
        for (int i = 0; i < intStrs.length; i++) {
			tmp = "";
			
			for (int j = s; j < s + l; j++) {
				tmp += intStrs[i].charAt(j);
			}
			
			num = Integer.parseInt(tmp);
			
			if (num > k) {
				answer.add(num);
			}
		}
        
        return answer.stream().mapToInt(x -> x).toArray();
    }
}