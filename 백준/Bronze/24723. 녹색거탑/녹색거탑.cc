#include <iostream>
using namespace std;

long power(long times) {
    long result = 1;

    while (times-- > 0) {
        result *= 2;
    }

    return result;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(NULL);

    int N;
    cin >> N;

    cout << power(N);

    return 0;
}
