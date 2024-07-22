#include <iostream>
using namespace std;

int scores[1000];

int main(void) {
    int C, tmp;
    double N, upper, sum, avg;
    cin >> C;

    for (int i = 0; i < C; i++)
    {
        cin >> N;

        sum = 0;

        for (int j = 0; j < N; j++)
        {
            cin >> tmp;
            scores[j] = tmp;
            sum += tmp;
        }
        
        avg = sum / N;
        upper = 0;

        for (int j = 0; j < N; j++)
        {
            if (scores[j] > avg) upper += 1000000;
        }

        int answer = upper / N;
        int temp = answer % 10;

        if (temp >= 5) answer += 10;
        
        answer /= 10;

        cout << double(answer) / 1000 << '%' << endl;
    }

    return 0;
}