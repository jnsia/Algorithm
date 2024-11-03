class Solution
{
    public int solution(int n, int a, int b)
    {
        int answer = 0;
        
        a = a - 1;
        b = b - 1;
        
        if (a > b) {
            int temp = a;
            a = b;
            b = temp;
        }
        
        while (a > 0 || b > 0) {
            answer++;
            
            if (a % 2 == 0 && b == a + 1) break;
            
            a /= 2;
            b /= 2;
        }

        return answer;
    }
}