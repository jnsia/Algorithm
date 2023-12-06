#include <iostream>
using namespace std;

char OX[81];

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(NULL);
    
    int N;
    cin >> N;

    for (int tc = 0; tc < N; tc++)
    {
        cin >> OX;
        
        int ans = 0;
        int cnt = 1;

        for (int i = 0; i < 81; i++)
        {
            if (OX[i] == NULL) break;

            if (OX[i] == 'O') {
                ans += cnt;
                cnt++;
            }
            else {
                cnt = 1;
            }
        }

        cout << ans << "\n";
    }

    return 0;
}
