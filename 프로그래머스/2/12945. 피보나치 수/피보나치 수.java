class Solution {
    static int[] pibos = new int[100001];
    static int mod = 1234567;
    
    public int solution(int n) {
        int answer = 0;
        
        pibos[1] = 1;
        pibos[2] = 1;
        pibos[3] = 2;
        
        answer = pibo(n);
        
        return answer;
    }
    
    private int pibo(int n) {
        if (n == 0) {
            return 0;
        }
        
        if (n == 1 || n == 2) {
            return 1;
        }
        
        if (pibos[n] > 0) {
            return pibos[n];
        }
        
        pibos[n] = (pibo(n - 1) + pibo(n - 2)) % mod;
        
        return pibos[n] % mod;
    }
}