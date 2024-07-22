class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int p = 0;
        int y = 0;
        
        for(int i = 0; i < s.length(); i++){
            
            if (s.charAt(i)=='p' || s.charAt(i)=='P'){
                p += 1;
                System.out.println(p + "p");
            }else if(s.charAt(i)=='y' || s.charAt(i)=='Y'){
                y += 1;
                System.out.println(y + "y");
                
            }
        }
        if(p == y){
            answer = true;
        }else{
            answer = false;
        }
        return answer;
    }
}