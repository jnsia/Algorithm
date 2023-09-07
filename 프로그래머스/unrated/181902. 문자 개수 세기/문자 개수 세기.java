class Solution {
    public int[] solution(String my_string) {
        int[] answer = new int[52];
        int tmp;
        char tmp_chr;
        
        for (int i = 0; i < my_string.length(); i++) {
            tmp_chr = my_string.charAt(i);
            tmp = (int)tmp_chr;
            
            if (tmp >= 65 && tmp <= 90) {
                answer[tmp - 65] += 1;
            } else {
                answer[tmp - 97 + 26] += 1;
            }
        }
        
        System.out.println((int)'A');
        System.out.println((int)'Z');
        System.out.println((int)'a');
        System.out.println((int)'z');
        
        return answer;
    }
}