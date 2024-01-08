#include <iostream>
#include <cmath>
using namespace std;

char board[10][10];

int main() {
    int N, M;
    cin >> N >> M;

    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(NULL);

    
    for (int i = 0; i < N; i++) {
        cin >> board[i];
    }

    int res = -1;

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            for (int a = -N; a < N; ++a) {
                for (int b = -M; b < M; ++b) {
                    if (a == 0 && b == 0) {
                        continue;
                    }

                    int num = 0;
                    int x = i, y = j;

                    while (0 <= x && x < N && 0 <= y && y < M) {
                        num *= 10;
                        num += int(board[x][y]) - int('0');
                        double temp = sqrt(num);

                        if (temp == int(temp)) {
                            res = max(num, res);
                        }

                        x += a;
                        y += b;
                    }
                }
            }
        }
    }

    cout << res << endl;

    return 0;
}