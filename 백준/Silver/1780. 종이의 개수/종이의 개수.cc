#include <iostream>
using namespace std;

int N;
short paper[2188][2188];

int minus_sum = 0;
int zero_sum = 0;
int plus_sum = 0;

static void dfs(int size, int x, int y) {
    if (size == 0) return;
    
    int minus = 0;
    int zero = 0;
    int plus = 0;

    for (int i = x; i < x + size; i++)
    {
        for (int j = y; j < y + size; j++) {
            if (paper[i][j] == -1) minus++;
            else if (paper[i][j] == 0) zero++;
            else plus++;
        }
    }

    int sum = minus + zero + plus;

    if (minus == sum) {
        minus_sum++;
        return;
    }
    else if (zero == sum) {
        zero_sum++;
        return;
    }
    else if (plus == sum) {
        plus_sum++;
        return;
    }

    int temp = size / 3;

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            dfs(temp, x + temp * i, y + temp * j);
        }
    }

    return;
}

int main() {
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(false);

    cin >> N;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++) {
            cin >> paper[i][j];
        }
    }

    dfs(N, 0, 0);

    cout << minus_sum << "\n";
    cout << zero_sum << "\n";
    cout << plus_sum << "\n";

    return 0;
}
