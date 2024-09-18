import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        StringBuilder sb = new StringBuilder(s);
        
        if(s.charAt(0) == ' '){
            sb.setCharAt(1, Character.toLowerCase(s.charAt(1)));
        }

        // 이거는 첫 글자가 문자일때만 따로 조건문 해놓은거야
        // 내가 첫번째 글자를 처리하려니 자꾸 index오류 떠서..
        if(Character.isLetter(s.charAt(0)) && Character.isLowerCase(s.charAt(0))){
            sb.setCharAt(0, Character.toUpperCase(s.charAt(0)));
        }
        
        for(int i = 1; i < s.length(); i++){
            // 문자일때만 대문자, 소문자 검증
            if(Character.isLetter(s.charAt(i))){
                if(s.charAt(i - 1) == ' '){
                    if(Character.isLowerCase(s.charAt(i))){
                        sb.setCharAt(i, Character.toUpperCase(s.charAt(i)));
                    }
                }else{
                    if(Character.isUpperCase(s.charAt(i))){
                        sb.setCharAt(i, Character.toLowerCase(s.charAt(i)));
                    }
                }
            }
        }
        answer = sb.toString();
        return answer;
    }
}