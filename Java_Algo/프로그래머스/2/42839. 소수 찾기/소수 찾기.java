import java.lang.Math;
import java.util.*;

class Solution {
    
    static int MAX = 10000000;
    static int[] primes = new int[MAX];
    static int[] visited = new int[10];
    static List<Integer> list = new ArrayList<>();
    
    public int solution(String numbers) {
        int answer = 0;
        
        dfs("", numbers, 0);
        
        for (int i = 0; i < list.size(); i++) {
            System.out.println(list.get(i));
            if (isPrime(list.get(i))) {
                answer++;
            }
        }
                
        return answer;
    }
    
    public void dfs(String res, String numbers, int idx) {
        if (idx == numbers.length()) {
            return;
        }
        
        for (int i = 0; i < numbers.length(); i++) {
            if (visited[i] == 0) {
                visited[i] = 1;
                
                String temp = res + numbers.charAt(i);
                int temp2 = convertStringToInt(temp);
                Boolean isExist = false;
                
                for (int j = 0; j < list.size(); j++) {
                    if (list.get(j) == temp2) {
                        isExist = true;
                    }
                }
                
                if (!isExist) {
                    list.add(temp2);
                }
                
                dfs(res, numbers, idx + 1);
                dfs(temp, numbers, idx + 1);
                visited[i] = 0;
            }
        }
    }
    
    public int power(int times) {
        int res = 1;
        
        for (int i = 0; i < times; i++) {
            res *= 10;
        }
        
        return res;
    }
    
    public int convertStringToInt(String number) {
        int res = 0;
        
        for (int i = number.length(); i > 0; i--) {
            res += (number.charAt(i - 1) - '0') * power(i - 1);
        }
        
        return res;
    }
    
    public Boolean isPrime(int num) {
        if (num == 0 || num == 1) {
            return false;
        }
        
        Boolean res = true;
        int sqr = (int) Math.sqrt(num);
        
        for (int i = 2; i < sqr + 1; i++) {
            if (num % i == 0) {
                res = false;
                break;
            }
        }
        
        return res;
    }
    
    
}