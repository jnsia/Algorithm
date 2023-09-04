class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[arr.length];
        int i, j, tmp;
        
        for (int x = 0; x < queries.length; x++) {			
        	i = queries[x][0];
        	j = queries[x][1];

        	tmp = arr[i];
        	arr[i] = arr[j];
        	arr[j] = tmp;
        }
        
        answer = arr;
        
        return answer;
    }
}