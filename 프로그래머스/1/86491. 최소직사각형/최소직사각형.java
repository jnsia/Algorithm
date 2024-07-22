class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        
        int longer = 0;
        int shorter = 0;
        
        for (int[] size: sizes) {
            int a = size[0];
            int b = size[1];
            int temp;
            
            if (a < b) {
                temp = a;
                a = b;
                b = temp;
            }
            
            if (a > longer) longer = a;
            if (b > shorter) shorter = b;
        }
        
        answer = longer * shorter;
        
        return answer;
    }
}