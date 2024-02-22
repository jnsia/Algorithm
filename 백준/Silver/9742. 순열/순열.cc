#include <iostream>
using namespace std;

int N, length;
char str[11];
char result[11];
char answer[11];

int perm_count;
int dp[11];
int collected[11];

static void permutation(int depth) {
    if (depth == length) {
        if (N == perm_count) {
            for (int i = 0; i < length; i++)
            {
                answer[i] = result[i];
            }
        }

        perm_count++;

        return;
    }

    for (int i = 0; i < length; i++)
    {
        if (collected[i] == 0) {
            collected[i] = 1;
            result[depth] = str[i];
            permutation(depth + 1);
            collected[i] = 0;
        }
    }
}

int main() {
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(false);

    dp[1] = 1;

    for (int i = 2; i < 11; i++)
    {
        dp[i] = dp[i - 1] * i;
    }

    while (true)
    {
        cin >> str >> N;

        perm_count = 1;

        for (int i = 0; i < 11; i++)
        {
            length = i;
            if (str[i] == NULL) break;
        }

        if (cin.eof()) break;

        if (dp[length] < N) {
            for (int i = 0; i < length; i++)
            {
                cout << str[i];
            }
            cout << " " << N << " = ";
            cout << "No permutation" << "\n";
        }
        else {
            permutation(0);
            for (int i = 0; i < length; i++)
            {
                cout << str[i];
            }
            cout << " " << N << " = ";
            for (int i = 0; i < length; i++)
            {
                cout << answer[i];
            }
            cout << "\n";
        }
    }

    return 0;
}
