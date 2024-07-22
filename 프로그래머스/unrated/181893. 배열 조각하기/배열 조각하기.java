import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[] query) {
        List<Integer> answer = new ArrayList<Integer>();
        int tmp;
        
        for (int i = 0; i < query.length; i++) {
            List<Integer> tmp_arr = new ArrayList<Integer>();
            tmp = query[i];
            
            if (i % 2 == 0) {
                for (int j = 0; j <= tmp; j++) {
                    tmp_arr.add(arr[j]);
                }
            } else {
                for (int j = tmp; j < arr.length; j++) {
                    tmp_arr.add(arr[j]);
                }
            }
            
            arr = tmp_arr.stream().mapToInt(x -> x).toArray();
        }
        
        System.out.println(arr);
        
        return arr;
    }
}