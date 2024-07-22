#include <iostream>
using namespace std;

long gcd(long a, long b) {
    long r;

    while (b != 0) {
        r = a % b;
        a = b;
        b = r;
    }

    return a;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(NULL);

    long A, B;

    cin >> A >> B;

    cout << (A * B) / gcd(A, B) << "\n";

    return 0;
}
