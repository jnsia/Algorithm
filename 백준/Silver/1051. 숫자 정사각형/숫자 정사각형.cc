#include <iostream>
using namespace std;

char board[51][51];

int main() {
    int N, M;
    cin >> N >> M;

    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(NULL);

    int answer = 0;
    int K = 51;

    if (N > M) K = M;
    else K = N;

    for (int i = 0; i < N; i++)
    {
        cin >> board[i];
    }
 
    for (int i = 0; i < K; i++)
    {
        for (int j = 0; j < N - i; j++)
        {
            for (int k = 0; k < M - i; k++)
            {
                if (board[j][k] == board[j + i][k] &&
                    board[j][k] == board[j][k + i] &&
                    board[j][k] == board[j + i][k + i]) answer = i + 1;
            }
        }
    }

    cout << answer * answer;
    
    return 0;
}