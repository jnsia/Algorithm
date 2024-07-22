class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        String tmp;
        
        for (int i = 0; i <= myString.length() - pat.length(); i++) {
            tmp = "";
            
            for (int j = 0; j < pat.length(); j++) {
                tmp += myString.charAt(i + j);
            }
            
            System.out.println(tmp);

            if (tmp.equals(pat)) {
                answer += 1;
            }
        }
        
        return answer;
    }
}