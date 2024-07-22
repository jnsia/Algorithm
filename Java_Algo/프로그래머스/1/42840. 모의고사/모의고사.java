import java.util.*;

class Solution {
    public int[] solution(int[] answers) {        
        List<Integer> result = new ArrayList<>();
        
        int sn1 = 5;
        int[] s1 = new int[] {1, 2, 3, 4, 5};
        
        int sn2 = 8;
        int[] s2 = new int[] {2, 1, 2, 3, 2, 4, 2, 5};
        
        int sn3 = 10;
        int[] s3 = new int[] {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        
        int s1s = 0;
        int s2s = 0;
        int s3s = 0;
        
        int i = 0;
        
        while (i < answers.length) {
            if (s1[i % sn1] == answers[i]) s1s++;
            if (s2[i % sn2] == answers[i]) s2s++;
            if (s3[i % sn3] == answers[i]) s3s++;    
            i++;
        }
        
        int max = -1;
        
        if (s1s >= max) max = s1s;
        if (s2s >= max) max = s2s;
        if (s3s >= max) max = s3s;
        
        if (s1s == max) result.add(1);
        if (s2s == max) result.add(2);
        if (s3s == max) result.add(3);
        
        int[] answer = new int[result.size()];
        
        for (int j = 0; j < answer.length; j++) {
            answer[j] = result.get(j);
        }
        
        return answer;
    }
}