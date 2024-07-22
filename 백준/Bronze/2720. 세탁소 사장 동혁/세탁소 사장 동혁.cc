#include <iostream>
using namespace std;

int main(void) {
    int T, C;
    cin >> T;

    for (int i = 0; i < T; i++)
    {
        cin >> C;
        int credit[4] = { 0, 0, 0, 0 };

        while (C > 0) {
            if (C / 25 > 0) {
                credit[0] += C / 25;
                C %= 25;
            }
            else if (C / 10 > 0) {
                credit[1] += C / 10;
                C %= 10;
            }
            else if (C / 5) {
                credit[2] += C / 5;
                C %= 5;
            }
            else {
                credit[3] += C;
                C = 0;
            }
        }

        for (int i = 0; i < 4; i++)
        {
            cout << credit[i] << " ";
        }
        cout << endl;
    }

    return 0;
}