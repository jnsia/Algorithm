#include <iostream>
using namespace std;

char chess[9][9];

int main()
{
    cin.tie(NULL);
    cout.tie(NULL);
    ios_base::sync_with_stdio(false);

    for (int i = 0; i < 8; i++)
    {
        cin >> chess[i];
    }

    int answer = 0;

    for (int i = 0; i < 8; i++)
    {
        for (int j = 0; j < 8; j++)
        {
            if ((i + j) % 2 == 0 && chess[i][j] == 'F') answer += 1;
        }
    }

    cout << answer;

    return 0;
}