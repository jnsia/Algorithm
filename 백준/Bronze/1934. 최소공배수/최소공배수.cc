#include <iostream>
using namespace std;

int gcd(int a, int b) {
    int r;

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

    int T, A, B;
    cin >> T;

    for (int i = 0; i < T; i++)
    {
        cin >> A >> B;

        cout << (A * B) / gcd(A, B) << "\n";
    }

    return 0;
}
