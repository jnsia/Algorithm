#include <iostream>
using namespace std;

#define min(a, b) (a < b) ? (a) : (b)

int N;
int s_arr[10001];
char arr_s[10001];
int t_arr[10001];
char arr_t[10001];
int dp[10001][10];

int f(int idx, int n_left) {
    if (idx > N)
        return 0;
    
    if (dp[idx][n_left] != -1)
        return dp[idx][n_left];
 
    int now = (s_arr[idx] + n_left) % 10;

    int m_left = (t_arr[idx] < now) ? t_arr[idx] - now + 10 : t_arr[idx] - now;
    int m_right = (now < t_arr[idx]) ? now - t_arr[idx] + 10 : now - t_arr[idx];
    
    dp[idx][n_left] = min(m_right + f(idx + 1, n_left), m_left + f(idx + 1, (n_left + m_left) % 10));
    
    return dp[idx][n_left];
}

int main(void) {
    cin >> N;

    cin >> arr_s;
    
    for (int i = 1; i <= N; i++) {
        s_arr[i] = int(arr_s[i - 1]) - int('0');
    }

    cin >> arr_t;
    
    for (int i = 1; i <= N; i++) {
        t_arr[i] = int(arr_t[i - 1]) - int('0');
    }

    for (int i = 0; i <= 10000; i++) {
        for (int j = 0; j < 10; j++)
            dp[i][j] = -1;
    }

    int ans = f(1, 0);
    
    cout << ans;
    
    return 0;
}