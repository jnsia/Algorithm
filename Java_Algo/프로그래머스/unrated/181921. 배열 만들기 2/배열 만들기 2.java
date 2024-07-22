import java.util.List;
import java.util.ArrayList;

class Solution {
    public int[] solution(int l, int r) {
        List<Integer> answer = new ArrayList<Integer>();
        String tmp;
        char tmp2;
        int cnt;
        
        for (int i = l; i <= r; i++) {
		    tmp = Integer.toString(i);
            cnt = 0;
            
            for (int j = 0; j < tmp.length(); j++) {
                tmp2 = tmp.charAt(j);
                if (tmp2 == '5' || tmp2 == '0') {
                    cnt += 1;
                }
            }
            
            if (cnt == tmp.length()) {
                answer.add(i);
            }
		}

        if (answer.isEmpty()) {
            answer.add(-1);
        }
        
        return answer.stream().mapToInt(i->i).toArray();
    }
}