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

    long A, B, C, D;

    cin >> A >> B >> C >> D;

    long gcd_num = gcd(B, D);

    long parent = (B * D) / gcd_num;
    long child = A * (parent / B) + C * (parent / D);

    gcd_num = gcd(parent, child);

    cout << child / gcd_num << " " << parent / gcd_num;

    return 0;
}
