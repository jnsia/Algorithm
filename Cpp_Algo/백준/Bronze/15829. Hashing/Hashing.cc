#include <iostream>
using namespace std;

int L;
char str[51];
const long long int R = 31;
const int M = 1234567891;

long long int power(int times) {
    if (times == 0) {
        return 1;
    }

    if (times == 1) {
        return R;
    }

    long long int temp = power(times / 2) % M;

    if (times % 2 == 0) {
        return (temp * temp) % M;
    }
    else {
        return ((temp * temp) % M * R) % M;
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(NULL);

    cin >> L;
    cin >> str;

    long long int answer = 0;

    for (int i = 0; i < L; i++)
    {
        answer += ((int(str[i]) - int('a') + 1) * power(i)) % M;
    }
    
    cout << answer % M;

    return 0;
}
