#include <iostream>
using namespace std;

#define min(x, y) ((x < y) ? (x) : (y))
#define max(x, y) ((x > y) ? (x) : (y))

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(NULL);

    int T, N, tmp;
    cin >> T;

    for (int i = 0; i < T; i++)
    {
        cin >> N;

        int min_v = 100;
        int max_v = -1;

        for (int j = 0; j < N; j++)
        {
            cin >> tmp;

            min_v = min(min_v, tmp);
            max_v = max(max_v, tmp);
        }

        cout << (max_v - min_v) * 2 << "\n";
    }

    return 0;
}
