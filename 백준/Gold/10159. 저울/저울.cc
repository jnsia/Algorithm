#include <iostream>
using namespace std;

int things[101][101];

int main()
{
    int N, M;
    cin >> N >> M;

    // 앞에가 더 무거운 것
    int a, b;

    for (int i = 0; i < M; i++)
    {
        cin >> a >> b;

        things[a][b] = 1;
        things[b][a] = -1;
    }

    for (int k = 1; k < N + 1; k++)
    {
        for (int i = 1; i < N + 1; i++)
        {
            for (int j = 1; j < N + 1; j++)
            {
                if ((things[i][k] != 0) && (things[i][k] == things[k][j])) {
                    things[i][j] = things[i][k];
                }
            }
        }
    }

    for (int i = 1; i < N + 1; i++)
    {
        int answer = -1;

        for (int j = 1; j < N + 1; j++)
        {
            if (things[i][j] == 0) answer += 1;
        }

        cout << answer << endl;
    }

    return 0;
}
