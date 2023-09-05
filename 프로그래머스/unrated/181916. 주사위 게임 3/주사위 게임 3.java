class Solution {
    public int pow(int num, int times) {
        int result = 1;
        
        for (int i = 0; i < times; i++) {
            result *= num;
        }
        
        return result;
    }
    
    public int abs(int num) {
        int result = num;
        
        if (num < 0) {
            result = -num;
        }
        
        return result;
    }
    
    public int solution(int a, int b, int c, int d) {
        int[] dice = new int[7];
        int answer = 0;
        int p = 0;
        int q = 0;
        int tmp;
        boolean is_dup = false;
        
        dice[a] += 1;
        dice[b] += 1;
        dice[c] += 1;
        dice[d] += 1;

        for (int i = 1; i < 7; i++) {
            tmp = dice[i];
            
            if (tmp == 4) {
                answer = 1111 * i;
                is_dup = true;
                break;
            } else if (tmp == 3) {
                p = i;
                
                for (int j = 1; j < 7; j++) {
                    if (dice[j] == 1) {
                        q = j;
                        answer = pow((10 * p + q), 2);
                        is_dup = true;
                        break;
                    }
                }
            } else if (tmp == 2) {                
                for (int j = 1; j < 7; j++) {
                    if (i != j && dice[j] == 1) {
                        if (p > 0) {
                            q = j;
                            answer = p * q;
                            is_dup = true;
                            break;
                        } else {
                            p = j;
                        }
                    }
                    
                    if (i != j && dice[j] == 2) {
                        p = i;
                        q = j;
                        answer = (p + q) * abs(p - q);
                        is_dup = true;
                        break;
                    }
                }
            }
        }
        
        if (!is_dup) {
            for (int i = 1; i < 7; i++) {
                if (dice[i] == 1) {
                    answer = i;
                    break;
                }
            }
        }
        
        return answer;
    }
}