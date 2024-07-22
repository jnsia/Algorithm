#include <iostream>
using namespace std;

int main() {
    int board[6][6] = {0};

    string tour[36];
    
    for (int i = 0; i < 36; ++i) {
        cin >> tour[i];
    }

    int sx = tour[0][0] - 'A';
    int sy = tour[0][1] - '1';
    board[sx][sy] = 1;

    bool flag = true;

    if (abs(tour[0][0] - tour[35][0]) == 2 && abs(tour[0][1] - tour[35][1]) == 1
        || abs(tour[0][0] - tour[35][0]) == 1 && abs(tour[0][1] - tour[35][1]) == 2) {
        for (int i = 1; i < 36; ++i) {
            int nx = tour[i][0] - 'A';
            int ny = tour[i][1] - '1';

            if (abs(nx - sx) == 2 && abs(ny - sy) == 1 || abs(nx - sx) == 1 && abs(ny - sy) == 2) {
                board[nx][ny] += 1;

                if (board[nx][ny] != 1) {
                    flag = false;
                    break;
                }
            } else {
                flag = false;
                break;
            }

            sx = nx;
            sy = ny;
        }
    } else {
        flag = false;
    }

    if (flag) {
        cout << "Valid" << endl;
    } else {
        cout << "Invalid" << endl;
    }

    return 0;
}
