class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[queries.length];
        int s, e, k;
        
        for (int i = 0; i < answer.length; i++) {			
        	s = queries[i][0];
        	e = queries[i][1];
        	k = queries[i][2];
        	
        	int tmp = -1;
        	
        	for (int j = s; j <= e; j++) {
				if (arr[j] > k && (tmp > arr[j] || tmp == -1)) {
					tmp = arr[j];
				}
			}
        	
        	answer[i] = tmp;
        }
        
        return answer;
    }
}