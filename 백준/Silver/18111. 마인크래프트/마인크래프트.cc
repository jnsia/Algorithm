#include <iostream>
using namespace std;

int N, M, B;
int apart[500][500];

int func(int height, int block) {
    int res = 0;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            int diff = apart[i][j] - height;

            if (diff > 0) {
                res += 2 * diff;
                block += diff;
            }
            else {
                res += (-1) * diff;
                block += diff;
            }
        }
    }

    if (block >= 0) {
        return res;
    }
    else {
        return 1000000000;
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(NULL);

    cin >> N >> M >> B;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cin >> apart[i][j];
        }
    }

    int max_time = 1000000000;
    int max_height = 0;

    for (int height = 0; height < 257; height++)
    {
        int res = func(height, B);

        if (max_time >= res) {
            max_time = res;
            max_height = height;
        }
    }

    cout << max_time << " " << max_height;

    return 0;
}