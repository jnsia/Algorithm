#include <iostream>
using namespace std;

int gcd(int x, int y) {
    int r;

    while (y != 0) {
        r = x % y;
        x = y;
        y = r;
    }

    return x;
}

int divi[50];

int main()
{
    cin.tie(NULL);
    cout.tie(NULL);
    ios_base::sync_with_stdio(false);

    int N;
    cin >> N;

    int min_v = 1000001; 
    int max_v = 1;

    for (int i = 0; i < N; i++)
    {
        cin >> divi[i];

        if (divi[i] > max_v) max_v = divi[i];
        if (divi[i] < min_v) min_v = divi[i];
    }

    long long int answer = divi[0];
    int temp;

    for (int i = 1; i < N; i++)
    {
        temp = gcd(answer, divi[i]);
        answer = (answer * divi[i]) / temp;
    }

    if (answer == max_v) answer *= min_v;

    cout << answer;

    return 0;
}
