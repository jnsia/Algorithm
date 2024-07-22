#include <iostream>
using namespace std;

#define max(x, y) ((x > y) ? x : y);

int N;
int arr[10];
short collected[10];
int board[50][10];
int base[3];
int answer = 0;

void comb(int idx) {
    if (idx == 10) {
        int out = 0;
        int score = 0;
        int player = 1;

        for (int i = 0; i < N; i++)
        {
            out = 0;

            for (int j = 0; j < 3; j++)
            {
                base[j] = 0;
            }

            while (out < 3) {
                int now = board[i][arr[player]];

                if (now == 0) out++;
                else if (now == 1) {
                    score += base[2];
                    base[2] = base[1];
                    base[1] = base[0];
                    base[0] = 1;
                }
                else if (now == 2) {
                    score += base[2] + base[1];
                    base[2] = base[0];
                    base[1] = 1;
                    base[0] = 0;
                }
                else if (now == 3) {
                    score += base[2] + base[1] + base[0];
                    base[2] = 1;
                    base[1] = 0;
                    base[0] = 0;
                }
                else {
                    score += base[2] + base[1] + base[0] + 1;
                    base[2] = 0;
                    base[1] = 0;
                    base[0] = 0;
                }

                player++;

                if (player > 9) player = 1;
            }

            answer = max(answer, score);
        }

        return;
    }
    
    if (idx == 4) {
        comb(idx + 1);
        return;
    }

    for (int i = 1; i < 10; i++)
    {
        if (collected[i] == 0) {
            arr[idx] = i;
            collected[i] = 1;
            comb(idx + 1);
            collected[i] = 0;
        }
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(NULL);
    
    cin >> N;

    collected[1] = 1;
    arr[4] = 1;

    for (int i = 0; i < N; i++)
    {
        for (int j = 1; j < 10; j++) {
            cin >> board[i][j];
        }
    }

    comb(1);

    cout << answer;

    return 0;
}
