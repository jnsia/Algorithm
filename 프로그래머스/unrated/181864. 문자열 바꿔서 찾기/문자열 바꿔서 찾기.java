class Solution {
	public int solution(String myString, String pat) {
        int answer = 0;
        String newString = "";
        
        for (int i = 0; i < myString.length(); i++) {
			if (myString.charAt(i) == 'A') {
				newString += "B";
			} else {
				newString += "A";
			}
		}
        
        System.out.println(newString);
        
        if (newString.indexOf(pat) >= 0) {
        	answer = 1;
        }
        
        return answer;
    }
}