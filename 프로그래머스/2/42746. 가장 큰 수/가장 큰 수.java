import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        
        String[] arr = new String[numbers.length];
        
        int i = 0;
        String temp = "";
        
        for (int number: numbers) {
            if (number == 0) {
                arr[i++] = "0";
                continue;
            }
            
            while (number > 0) {
                temp = (number % 10) + temp;
                number /= 10;
            }
            
            arr[i++] = temp;
            temp = "";
        }
        
        Arrays.sort(arr, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return (o2 + o1).compareTo(o1 + o2);
            }
        });

        for (String str: arr) {
            if (answer.length() == 0 && str.equals("0")) {
                continue;
            }
            answer += str;
        }
        
        if (answer.equals("")) {
            answer = "0";
        }
        
        return answer;
    }
}