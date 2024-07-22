#include <iostream>
using namespace std;

int apart[15][15];

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(NULL);

    int T, k, n;
    cin >> T;

    for (int i = 1; i <= 14; i++)
    {
        apart[0][i] = i;
    }

    for (int i = 1; i <= 14; i++)
    {
        for (int j = 1; j <= 14; j++)
        {
            apart[i][j] = apart[i - 1][j] + apart[i][j - 1];
        }
    }

    for (int i = 0; i < T; i++)
    {
        cin >> k >> n;

        cout << apart[k][n] << "\n";
    }

    return 0;
}
